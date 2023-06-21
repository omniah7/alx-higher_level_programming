-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
ALTER DATABASE hbtn_0c_0
    CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table
    CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
    ALTER COLUMN name {
      CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
    };
