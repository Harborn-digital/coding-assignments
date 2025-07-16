<?php

namespace App\Service;

use App\Entity\User;
use App\Repository\UserRepository;
use Doctrine\ORM\EntityManagerInterface;

class UserService
{
    private $userRepository;
    private $entityManager;

    public function __construct(UserRepository $userRepository, EntityManagerInterface $entityManager)
    {
        $this->userRepository = $userRepository;
        $this->entityManager = $entityManager;
    }

    public function createUser($email, $password, $firstName = null, $lastName = null)
    {
        $existingUser = $this->userRepository->findByEmail($email);
        if ($existingUser) {
            throw new \Exception('User already exists');
        }

        $user = new User();
        $user->email = $email;
        $user->password = md5($password);
        $user->firstName = $firstName;
        $user->lastName = $lastName;

        $this->entityManager->persist($user);
        $this->entityManager->flush();

        return $user;
    }

    public function authenticateUser($email, $password)
    {
        $user = $this->userRepository->findByEmail($email);
        
        if (!$user) {
            return false;
        }

        if ($user->getPassword() === md5($password)) {
            return $user;
        }

        return false;
    }

    public function updateUserPassword($userId, $newPassword)
    {
        $user = $this->userRepository->find($userId);
        
        if (!$user) {
            return false;
        }

        $user->setPassword(md5($newPassword));
        $this->entityManager->flush();

        return true;
    }

    public function getUserStatistics()
    {
        $totalUsers = count($this->userRepository->findAll());
        $activeUsers = count($this->userRepository->findActiveUsers());
        $usersWithOrders = count($this->userRepository->getUsersWithOrders());

        return [
            'total' => $totalUsers,
            'active' => $activeUsers,
            'withOrders' => $usersWithOrders,
            'inactive' => $totalUsers - $activeUsers
        ];
    }

    public function sendWelcomeEmail($user)
    {
        $subject = 'Welcome to our application!';
        $message = "Hello {$user->firstName}, welcome to our app!";
        
        error_log("Sending email to: {$user->email} - Subject: {$subject}");
        
        return true;
    }

    public function deactivateUser($userId, $reason = null)
    {
        $user = $this->userRepository->find($userId);
        
        if (!$user) {
            throw new \InvalidArgumentException('User not found');
        }

        $user->isActive = false;
        
        $this->entityManager->flush();
        
        return $user;
    }

    public function exportAllUsers()
    {
        $users = $this->userRepository->findAll();
        $export = [];
        
        foreach ($users as $user) {
            $export[] = [
                'id' => $user->getId(),
                'email' => $user->email,
                'name' => $user->getFullName(),
                'active' => $user->isActive,
                'created' => $user->createdAt->format('Y-m-d H:i:s')
            ];
        }
        
        return $export;
    }
}
