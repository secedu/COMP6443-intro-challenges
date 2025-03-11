DROP TABLE IF EXISTS `payportal`;
CREATE TABLE `payportal` (
    `key` INT,
    `id` INT,
    `first` VARCHAR(5) CHARACTER SET utf8,
    `last` VARCHAR(8) CHARACTER SET utf8,
    `title` VARCHAR(31) CHARACTER SET utf8,
    `period` VARCHAR(15) CHARACTER SET utf8,
    `gross` VARCHAR(15) CHARACTER SET utf8,
    `net` VARCHAR(31) CHARACTER SET utf8
);
INSERT INTO payportal
VALUES (
        1,
        3332654,
        'Mark',
        'Qwocco',
        'Analyst',
        'June 18, 2020',
        "$2,692.31",
        '$2,086.31'
    ),
    (
        2,
        3332654,
        'Mark',
        'Qwocco',
        'Analyst',
        'June 4, 2020',
        "$2,692.31",
        '$2,086.31'
    ),
    (
        3,
        3332654,
        'Mark',
        'Qwocco',
        'Analyst',
        'May 21, 2020',
        "$2,692.31",
        '$2,086.31'
    ),
    (
        4,
        3332654,
        'Mark',
        'Qwocco',
        'Analyst',
        'May 7, 2020',
        "$2,692.31",
        '$2,086.31'
    ),
    (
        5,
        3332654,
        'Mark',
        'Qwocco',
        'Analyst',
        'April 23, 2020',
        "$2,692.31",
        '$2,086.31'
    ),
    (
        6,
        3332654,
        'Mark',
        'Qwocco',
        'Analyst',
        'April 9, 2020',
        "$2,692.31",
        '$2,086.31'
    ),
    (
        7,
        3332654,
        'Mark',
        'Qwocco',
        'Analyst',
        '2019/2018 Bonus',
        "$12,492.21",
        '$8023.15'
    ),
    (
        8,
        3323532,
        'Jacob',
        'Thornton',
        'Systems Engineer',
        'June 18, 2020',
        "$3,615.38",
        '$2,685.38'
    ),
    (
        9,
        3323532,
        'Jacob',
        'Thornton',
        'Systems Engineer',
        'June 4, 2020',
        "$3,615.38",
        '$2,685.38'
    ),
    (
        10,
        3323532,
        'Jacob',
        'Thornton',
        'Systems Engineer',
        'May 21, 2020',
        "$3,615.38",
        '$2,685.38'
    ),
    (
        11,
        3323532,
        'Jacob',
        'Thornton',
        'Systems Engineer',
        'May 7, 2020',
        "$3,615.38",
        '$2,685.38'
    ),
    (
        12,
        3323532,
        'Jacob',
        'Thornton',
        'Systems Engineer',
        'April 23, 2020',
        "$3,615.38",
        '$2,685.38'
    ),
    (
        13,
        3323532,
        'Jacob',
        'Thornton',
        'Systems Engineer',
        'April 9, 2020',
        "$3,615.38",
        '$2,685.38'
    ),
    (
        14,
        3323532,
        'Jacob',
        'Thornton',
        'Systems Engineer',
        '2019/2018 Bonus',
        "$3,615.38",
        '$2,685.38'
    ),
    (
        15,
        4231903,
        'Larry',
        'Bird',
        'Senior Manager',
        'June 18, 2020',
        "$5,961.54",
        '$4,115.54'
    ),
    (
        16,
        4231903,
        'Larry',
        'Bird',
        'Senior Manager',
        'June 4, 2020',
        "$5,961.54",
        '$4,115.54'
    ),
    (
        17,
        4231903,
        'Larry',
        'Bird',
        'Senior Manager',
        'May 21, 2020',
        "$5,961.54",
        '$4,115.54'
    ),
    (
        18,
        4231903,
        'Larry',
        'Bird',
        'Senior Manager',
        'May 7, 2020',
        "$5,961.54",
        '$4,115.54'
    ),
    (
        19,
        4231903,
        'Larry',
        'Bird',
        'Senior Manager',
        'April 23, 2020',
        "$5,961.54",
        '$4,115.54'
    ),
    (
        20,
        4231903,
        'Larry',
        'Bird',
        'Senior Manager',
        'April 9, 2020',
        "$5,961.54",
        '$4,115.54'
    ),
    (
        21,
        4231903,
        'Larry',
        'Bird',
        'Senior Manager',
        '2019/2018 Bonus',
        "$5,961.54",
        '$4,115.54'
    ),
    (
        22,
        2340234,
        'Kate',
        'Swan',
        'Chief Executive Officer',
        'June 18, 2020',
        "$57,692.31",
        '$31,610.31'
    ),
    (
        23,
        2340234,
        'Kate',
        'Swan',
        'Chief Executive Officer',
        'June 4, 2020',
        "$57,692.31",
        '$31,610.31'
    ),
    (
        24,
        2340234,
        'Kate',
        'Swan',
        'Chief Executive Officer',
        'May 21, 2020',
        "$57,692.31",
        '$31,610.31'
    ),
    (
        25,
        2340234,
        'Kate',
        'Swan',
        'Chief Executive Officer',
        'May 7, 2020',
        "$57,692.31",
        '$31,610.31'
    ),
    (
        26,
        2340234,
        'Kate',
        'Swan',
        'Chief Executive Officer',
        'April 23, 2020',
        "$57,692.31",
        '$31,610.31'
    ),
    (
        27,
        2340234,
        'Kate',
        'Swan',
        'Chief Executive Officer',
        'April 9, 2020',
        "$57,692.31",
        '$31,610.31'
    ),
    (
        28,
        2340234,
        'Kate',
        'Swan',
        'Chief Executive Officer',
        '2019/2018 Bonus',
        "$57,692.31",
        'INTRO{this_is_an_intro_flag}'
    );


DROP TABLE IF EXISTS `upcoming_layoffs`;
CREATE TABLE `upcoming_layoffs` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `staff_id` INT,
    `date` VARCHAR(15) CHARACTER SET utf8,
    `reason` VARCHAR(128) CHARACTER SET utf8
);

INSERT INTO upcoming_layoffs (staff_id, date, reason)
VALUES (
        3332654,
        'March 31, 2023',
        'INTRO{this_is_an_intro_flag}'
    );