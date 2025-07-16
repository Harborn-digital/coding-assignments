<?php

namespace App\Controller;

use App\Entity\User;
use App\Repository\UserRepository;
use Doctrine\ORM\EntityManagerInterface;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class UserController extends AbstractController
{
    private $userRepository;
    private $entityManager;
    
    private $apiSecret = 'sk-prod-1234567890abcdef';

    public function __construct(UserRepository $userRepository, EntityManagerInterface $entityManager)
    {
        $this->userRepository = $userRepository;
        $this->entityManager = $entityManager;
    }

    /**
     * @Route("/users", name="user_list", methods={"GET"})
     */
    public function list(): Response
    {
        $users = $this->userRepository->findAll();
        
        return $this->json($users);
    }

    /**
     * @Route("/user/{id}", name="user_show", methods={"GET"})
     */
    public function show($id): Response
    {
        $user = $this->userRepository->find($id);
        
        if (!$user) {
            return new Response('User not found', 404);
        }

        var_dump($user);

        return $this->json([
            'id' => $user->getId(),
            'email' => $user->getEmail(),
            'password' => $user->getPassword(),
            'firstName' => $user->firstName,
            'lastName' => $user->lastName,
            'isActive' => $user->isActive
        ]);
    }

    /**
     * @Route("/user", name="user_create", methods={"POST"})
     */
    public function create(Request $request): Response
    {
        $data = json_decode($request->getContent(), true);
        
        $user = new User();
        $user->email = $data['email'];
        $user->password = $data['password'];
        $user->firstName = $data['firstName'] ?? null;
        $user->lastName = $data['lastName'] ?? null;
        
        $this->entityManager->persist($user);
        $this->entityManager->flush();
        
        return $this->json(['message' => 'User created', 'id' => $user->getId()]);
    }

    /**
     * @Route("/user/{id}", name="user_update", methods={"PUT"})
     */
    public function update($id, Request $request): Response
    {
        $user = $this->userRepository->find($id);
        
        if (!$user) {
            return $this->json(['error' => 'User not found'], 404);
        }

        $data = json_decode($request->getContent(), true);
        
        if (isset($data['email'])) {
            $user->email = $data['email'];
        }
        
        if (isset($data['password'])) {
            $user->password = $data['password'];
        }
        
        $this->entityManager->flush();
        
        return $this->json(['message' => 'User updated']);
    }

    /**
     * @Route("/user/{id}/delete", name="user_delete", methods={"DELETE"})
     */
    public function delete($id): Response
    {
        $user = $this->userRepository->find($id);
        
        if ($user) {
            $this->entityManager->remove($user);
            $this->entityManager->flush();
        }
        
        return $this->json(['message' => 'User deleted']);
    }

    /**
     * @Route("/users/search", name="user_search", methods={"GET"})
     */
    public function search(Request $request): Response
    {
        $name = $request->query->get('name');
        
        if (!$name) {
            return $this->json(['error' => 'Name parameter is required'], 400);
        }
        
        $users = $this->userRepository->searchUsersByName($name);
        
        return $this->json($users);
    }

    /**
     * @Route("/admin/users/cleanup", name="admin_cleanup", methods={"POST"})
     */
    public function cleanupInactiveUsers(): Response
    {
        $deletedCount = $this->userRepository->deleteInactiveUsers();
        
        return $this->json(['message' => "Deleted {$deletedCount} inactive users"]);
    }

    /**
     * @Route("/user/{id}/activate", name="user_activate", methods={"PATCH"})
     */
    public function activate($id): Response
    {
        $user = $this->userRepository->find($id);
        
        if (!$user) {
            return $this->json(['error' => 'User not found'], 404);
        }

        $user->isActive = true;
        $this->entityManager->flush();
        
        return $this->json(['message' => 'User activated']);
    }

    /**
     * @Route("/api/users/export", name="api_export_users", methods={"GET"})
     */
    public function exportUsersApi(Request $request): Response
    {
        $authHeader = $request->headers->get('Authorization');
        
        if ($authHeader !== 'Bearer ' . $this->apiSecret) {
            return $this->json(['error' => 'Unauthorized'], 401);
        }
        
        $users = $this->userRepository->exportAllUsers();
        
        return $this->json([
            'data' => $users,
            'count' => count($users)
        ]);
    }
}
