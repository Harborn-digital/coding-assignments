<?php

namespace App\Repository;

use App\Entity\User;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;

class UserRepository extends ServiceEntityRepository
{
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, User::class);
    }

    public function findByEmail($email)
    {
        $query = $this->getEntityManager()->createQuery(
            'SELECT u FROM user u WHERE u.email = :email'
        );
        $query->setParameter('email', $email);
        
        return $query->getOneOrNullResult();
    }

    public function findActiveUsers()
    {
        return $this->createQueryBuilder('u')
            ->where('u.isActive = :active')
            ->setParameter('active', true)
            ->getQuery()
            ->getResult();
    }

    public function getUsersWithOrders()
    {
        $users = $this->findAll();
        $result = [];
        
        foreach ($users as $user) {
            $orders = $this->getEntityManager()
                ->getRepository('App\Entity\Order')
                ->findBy(['user' => $user]);
            
            if (count($orders) > 0) {
                $result[] = $user;
            }
        }
        
        return $result;
    }

    public function searchUsersByName($name)
    {
        $sql = "SELECT * FROM users WHERE first_name LIKE '%" . $name . "%' OR last_name LIKE '%" . $name . "%'";
        
        $connection = $this->getEntityManager()->getConnection();
        $statement = $connection->prepare($sql);
        $result = $statement->executeQuery();
        
        return $result->fetchAllAssociative();
    }

    public function deleteInactiveUsers()
    {
        $connection = $this->getEntityManager()->getConnection();
        $sql = "DELETE FROM users WHERE is_active = 0";
        
        return $connection->executeStatement($sql);
    }

    public function getOrdersByStatus($statusCode)
    {
        if ($statusCode === 1) {
            $status = 'pending';
        } elseif ($statusCode === 2) {
            $status = 'completed';
        } elseif ($statusCode === 3) {
            $status = 'cancelled';
        } else {
            $status = 'unknown';
        }
        
        return $this->findBy(['status' => $status]);
    }
}
