-- Chat Messaging System - Emojis
-- Hali Imanpanah
-- A01424306


USE chat_messaging;
SHOW TABLES;


-- Add a table with a list of possible emojis.
CREATE TABLE emoji (
    emoji_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    image VARCHAR(100) NOT NULL
);

INSERT INTO emoji (emoji_id, name, image) VALUES
(1, 'thumbs up', 'thumbsup.png'),
(2, '100 percent', '100.png'),
(3, 'happy face', 'happy.png');


-- add a way to store a list of emojis for each message, and which user reacted.
CREATE TABLE message_reactions (
    message_id INT NOT NULL,
    emoji_id INT NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (message_id, emoji_id, user_id),
    FOREIGN KEY (emoji_id) REFERENCES emoji(emoji_id)
);


INSERT INTO message_reactions (message_id, emoji_id, user_id) VALUES
(1, 1, 2),
(1, 1, 3),
(1, 1, 4),
(1, 2, 2),
(1, 2, 4),
(1, 3, 4),
(1, 3, 5);

-- Write a query, to show all the users, their emoji reaction for a particular message
SELECT 
    mr.message_id,
    u.username,
    e.name AS emoji_name
FROM message_reactions mr
JOIN user u ON mr.user_id = u.user_id
JOIN emoji e ON mr.emoji_id = e.emoji_id
WHERE mr.message_id = 1
ORDER BY u.username, e.name;

-- Write a query to show a count of all the emojis that correspond to particular message
SELECT 
    mr.message_id,
    e.name AS emoji_name,
    COUNT(*) AS count
FROM message_reactions mr
JOIN emoji e ON mr.emoji_id = e.emoji_id
WHERE mr.message_id = 1
GROUP BY mr.message_id, e.name
ORDER BY count DESC, e.name;


-- Write a query to find the message(s) with the most (or tied for the most) number of emojis.
SELECT 
    message_id,
    COUNT(*) AS total_emojis
FROM message_reactions
GROUP BY message_id
ORDER BY total_emojis DESC
LIMIT 1;

-- Write a query to find the room(s) with the most (or tied for the most) number of emojis.
SELECT 
    ru.room_id,
    COUNT(*) AS total_emojis
FROM message_reactions mr
JOIN message m ON mr.message_id = m.message_id
JOIN room_user ru ON m.room_user_id = ru.room_user_id
GROUP BY ru.room_id
HAVING COUNT(*) = (
    SELECT COUNT(*) AS emoji_count
    FROM message_reactions mr2
    JOIN message m2 ON mr2.message_id = m2.message_id
    JOIN room_user ru2 ON m2.room_user_id = ru2.room_user_id
    GROUP BY ru2.room_id
    ORDER BY emoji_count DESC
    LIMIT 1
)
ORDER BY ru.room_id;
    

    
















