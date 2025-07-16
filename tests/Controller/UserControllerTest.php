<?php

namespace App\Tests\Controller;

use Symfony\Bundle\FrameworkBundle\Test\WebTestCase;

class UserControllerTest extends WebTestCase
{
    public function testUserList()
    {
        $client = static::createClient();
        $crawler = $client->request('GET', '/users');

        $this->assertEquals(200, $client->getResponse()->getStatusCode());
    }

    public function testUserCreation()
    {
        $client = static::createClient();
        
        $userData = [
            'email' => 'test@example.com',
            'password' => 'password123',
            'firstName' => 'John',
            'lastName' => 'Doe'
        ];
        
        $client->request(
            'POST',
            '/user',
            [],
            [],
            ['CONTENT_TYPE' => 'application/json'],
            json_encode($userData)
        );

        $this->assertEquals(200, $client->getResponse()->getStatusCode());
    }
}
