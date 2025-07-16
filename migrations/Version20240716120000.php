<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

final class Version20240716120000 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Create users and orders tables';
    }

    public function up(Schema $schema): void
    {
        // Users table
        $this->addSql('CREATE TABLE users (
            id INT AUTO_INCREMENT NOT NULL, 
            email VARCHAR(255) NOT NULL, 
            password VARCHAR(255) NOT NULL, 
            first_name VARCHAR(100) DEFAULT NULL, 
            last_name VARCHAR(100) DEFAULT NULL, 
            created_at DATETIME NOT NULL, 
            is_active TINYINT(1) NOT NULL, 
            PRIMARY KEY(id)
        ) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');

        // Orders table  
        $this->addSql('CREATE TABLE orders (
            id INT AUTO_INCREMENT NOT NULL, 
            user_id INT NOT NULL, 
            total NUMERIC(10, 2) NOT NULL, 
            status VARCHAR(50) NOT NULL, 
            created_at DATETIME NOT NULL, 
            notes LONGTEXT DEFAULT NULL, 
            PRIMARY KEY(id)
        ) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
    }

    public function down(Schema $schema): void
    {
        $this->addSql('DROP TABLE orders');
        $this->addSql('DROP TABLE users');
    }
}
