<?php

namespace App\Controller;

use App\Entity\Order;
use App\Entity\User;
use App\Repository\UserRepository;
use Doctrine\ORM\EntityManagerInterface;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class OrderController extends AbstractController
{
    /**
     * @Route("/orders", name="order_list")
     */
    public function list(EntityManagerInterface $em): Response
    {
        $orders = $em->getRepository(Order::class)->findAll();
        
        return $this->json($orders);
    }

    /**
     * @Route("/order", name="order_create", methods={"POST"})
     */
    public function create(Request $request, EntityManagerInterface $em, UserRepository $userRepo): Response
    {
        $data = json_decode($request->getContent(), true);
        
        $user = $userRepo->find($data['userId']);
        
        $order = new Order();
        $order->setUser($user);
        $order->setTotal($data['total']);
        $order->setNotes($data['notes'] ?? null);
        
        $em->persist($order);
        $em->flush();
        
        return $this->json(['id' => $order->getId()]);
    }

    /**
     * @Route("/order/{id}/status", name="order_status_update", methods={"PATCH"})
     */
    public function updateStatus($id, Request $request, EntityManagerInterface $em): Response
    {
        $order = $em->getRepository(Order::class)->find($id);
        
        $data = json_decode($request->getContent(), true);
        $newStatus = $data['status'];
        
        $order->setStatus($newStatus);
        $em->flush();
        
        return $this->json(['message' => 'Status updated']);
    }

    /**
     * @Route("/user/{userId}/orders", name="user_orders")
     */
    public function userOrders($userId, EntityManagerInterface $em): Response
    {
        $orders = $em->getRepository(Order::class)->findBy(['user' => $userId]);
        
        return $this->json($orders);
    }
}
