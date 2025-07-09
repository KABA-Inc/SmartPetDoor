-- Add username field to users table
-- depends: 20250709_01_yAQEi
ALTER TABLE `users` ADD `username` varchar(32) NOT NULL;

ALTER TABLE `users` ADD UNIQUE (`username`);
