USE chat_messaging;

-- Disable safe update mode
SET SQL_SAFE_UPDATES = 0;

-- Step 2: Set everyone's last_read_message_id to the max message_id
UPDATE room_user
SET last_read_message_id = (SELECT MAX(message_id) FROM message);

-- Re-enable safe update mode (optional)
SET SQL_SAFE_UPDATES = 1;

SELECT * FROM room_user;

USE chat_messaging;


USE chat_messaging;

-- Disable safe update mode
SET SQL_SAFE_UPDATES = 0;

-- Step 2: Set everyone's last_read_message_id to the max message_id
UPDATE room_user
SET last_read_message_id = (SELECT MAX(message_id) FROM message);

-- Re-enable safe update mode (optional)
SET SQL_SAFE_UPDATES = 1;

-- Step 3: List users and rooms where they have unread messages
SELECT ru.user_id, ru.room_id
FROM room_user ru
WHERE EXISTS (
    SELECT 1
    FROM message m
    JOIN room_user ru2 ON ru2.room_user_id = m.room_user_id
    WHERE ru2.room_id = ru.room_id
      AND m.message_id > ru.last_read_message_id
)
ORDER BY ru.user_id, ru.room_id;


USE chat_messaging;

-- Step 4: Add 4 new messages
INSERT INTO message 
VALUES 
(26,1,'2023-02-06 15:12:45','Perfect! See you all there!'),
(27,15,'2023-02-06 17:05:13','My cat sheds so much!'),
(28,22,'2023-02-06 18:41:23','I want to go to Reno!'),
(29,3,'2023-02-06 20:55:01','I can\'t make it. Have fun!');

USE chat_messaging;

-- Step 5: List users and rooms where they have unread messages
SELECT ru.user_id, ru.room_id
FROM room_user ru
WHERE EXISTS (
    SELECT 1
    FROM message m
    JOIN room_user ru2 ON ru2.room_user_id = m.room_user_id
    WHERE ru2.room_id = ru.room_id
      AND m.message_id > ru.last_read_message_id
)
ORDER BY ru.user_id, ru.room_id;







USE chat_messaging;

-- Count the number of unread messages per user per room
SELECT ru.user_id, ru.room_id, COUNT(*) AS num_messages_behind
FROM room_user ru
JOIN room_user ru2 ON ru2.room_id = ru.room_id
JOIN message m ON m.room_user_id = ru2.room_user_id
WHERE m.message_id > ru.last_read_message_id
GROUP BY ru.user_id, ru.room_id
ORDER BY ru.user_id, ru.room_id;






-- Step 6: 

