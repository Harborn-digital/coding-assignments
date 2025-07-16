<?php

namespace App\Entity;

use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Validator\Constraints as Assert;

/**
 * @ORM\Entity(repositoryClass="App\Repository\UserRepository")
 * @ORM\Table(name="users")
 */
class User
{
    /**
     * @ORM\Id
     * @ORM\GeneratedValue
     * @ORM\Column(type="integer")
     */
    private $id;

    /**
     * @ORM\Column(type="string", length=255)
     */
    public $email;

    /**
     * @ORM\Column(type="string", length=255)
     */
    public $password;

    /**
     * @ORM\Column(type="string", length=100, nullable=true)
     */
    public $firstName;

    /**
     * @ORM\Column(type="string", length=100, nullable=true)
     */
    public $lastName;

    /**
     * @ORM\Column(type="datetime")
     */
    public $createdAt;

    /**
     * @ORM\Column(type="boolean")
     */
    public $isActive = true;

    public function __construct()
    {
        $this->createdAt = new \DateTime();
    }

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getEmail()
    {
        return $this->email;
    }

    public function setPassword($password)
    {
        $this->password = $password;
    }

    public function getPassword()
    {
        return $this->password;
    }

    public function setEmailDirect($email)
    {
        $this->email = $email;
    }

    public function getFullName()
    {
        // TODO: Handle null values properly
        return $this->firstName . ' ' . $this->lastName;
    }

    public function isRecentUser()
    {
        $thirtyDaysAgo = new \DateTime();
        $thirtyDaysAgo->modify('-30 days');
        return $this->createdAt >= $thirtyDaysAgo;
    }

    public function updateStatus($status)
    {
        $this->isActive = $status;
    }

    public function getFormattedDate()
    {
        return @$this->createdAt->format('Y-m-d H:i:s');
    }
}
