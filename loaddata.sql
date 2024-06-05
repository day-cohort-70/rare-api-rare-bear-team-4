DROP TABLE IF EXISTS "Comments";

CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  "subject" varchar,
  "creation_date" date,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Comments ('author_id', 'post_id', 'content') VALUES ('1', '1', 'potato');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');
INSERT INTO "Users" 
  ("first_name", "last_name", "email", "bio", "username", "password", "profile_image_url", "created_on", "active") 
VALUES 
  ('novo', 'novo', 'novo@novo.com', 'A short bio about novo.', 'novo', 'novo', 'https://www.desertusa.com/dusablog/wp-content/uploads/jackrabbit-has-long-ears.jpg', '2023-05-20', 1);


INSERT INTO Posts (user_id, category_id, title, publication_date, image_url, content, approved)
VALUES (1, 2, 'Sample Post Title', '2024-05-28', 'https://example.com/sample-image.jpg', 'This is the content of the sample post.', 1);

INSERT INTO Categories (label)
VALUES ('Sample Category');

INSERT INTO Categories (label)
VALUES ('Technology');


INSERT INTO Users (first_name, last_name, email, bio, username, password, profile_image_url, created_on, active)
VALUES ('John', 'Doe', 'john.doe@example.com', 'A brief bio about John Doe.', 'johndoe', 'password123', 'https://example.com/profile-image.jpg', '2024-05-28', 1);

INSERT INTO Posts (user_id, category_id, title, publication_date, image_url, content, approved)
VALUES (3, 1, 'Exciting News in Tech', '2024-05-29', 'https://example.com/tech-news.jpg', 'This is an exciting update about the latest in technology.', 1);
INSERT INTO Posts (user_id, category_id, title, publication_date, image_url, content, approved)
VALUES (2, 4, 'Upcoming Events', '2024-06-01', 'https://example.com/upcoming-events.jpg', 'Here is a list of upcoming events you might be interested in.', 0);
INSERT INTO Posts (user_id, category_id, title, publication_date, image_url, content, approved)
VALUES (1, 2, 'Innovative Startup Ideas', '2024-05-30', 'https://example.com/startup-ideas.jpg', 'Exploring the most innovative startup ideas that are disrupting the market.', 1);

DELETE FROM "PostTags"
WHERE "id" = 40