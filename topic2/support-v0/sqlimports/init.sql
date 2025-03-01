CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    title TEXT,
    contents TEXT
);

-- Insert data into table
INSERT INTO tickets (user_id, contents)
VALUES (1, 'first ticket test!'),
    (1, 'ok it seems to be working'),
    (
        1,
        'How to use Ticket System\n\nIts trivial. You submit a ticket and theres your ticket'
    ),
    (1234, 'i want to open a savings account'),
    (567, 'how do I reset my online banking password'),
    (890, 'my debit card is not working'),
    (2345, 'i need help with a loan application'),
    (678, 'why was my transaction declined'),
    (123, 'i want to report a lost credit card'),
    (456, 'how can I increase my credit limit'),
    (
        890,
        'i have a question about my mortgage payment'
    ),
    (
        234,
        'what are the fees for international wire transfers'
    ),
    (
        678,
        'i want to dispute a charge on my statement'
    ),
    (1357, 'how do I set up direct deposit'),
    (
        2468,
        'i need assistance with my investment account'
    ),
    (3579, 'why is my account overdrawn'),
    (678, 'i want to close my checking account'),
    (890, 'how do I apply for a personal loan'),
    (
        1357,
        'what is the interest rate on my savings account'
    ),
    (2468, 'i need help with my tax documents'),
    (567, 'how can I transfer money between accounts'),
    (890, 'i want to know my credit score'),
    (1234, 'what should I do if I suspect fraud'),
    (567, 'how do I update my personal information'),
    (890, 'i want to set up account alerts'),
    (
        2345,
        'what are the benefits of a premium account'
    ),
    (678, 'i need help with mobile banking app'),
    (1357, 'how do I cancel a recurring payment'),
    (
        2468,
        'i want to know about your investment options'
    ),
    (890, 'why is my check taking so long to clear'),
    (567, 'i need to change my billing address'),
    (1234, 'how do I report a phishing email'),
    (678, 'i want to know about your loan rates'),
    (890, 'how can I get a replacement debit card'),
    (
        2345,
        'i have a question about my account statement'
    ),
    (
        678,
        'what is the process for applying for a mortgage'
    ),
    (1357, 'i want to set up a joint account'),
    (2468, 'how do I access my account from abroad'),
    (567, 'i need help with a wire transfer'),
    (890, 'what are the limits on my credit card'),
    (
        1234,
        'i want to know about your retirement accounts'
    ),
    (567, 'how do I dispute a transaction'),
    (
        890,
        'i need assistance with my business account'
    ),
    (
        2345,
        'what is the minimum balance for my account'
    ),
    (678, 'how do I enroll in paperless statements'),
    (
        1357,
        'i want to know about your insurance products'
    ),
    (2468, 'how can I improve my credit score'),
    (567, 'i need help with a loan payoff'),
    (890, 'what are the fees for using an ATM'),
    (1234, 'how do I set up a budget with my account'),
    (
        567,
        'i want to know about your student accounts'
    ),
    (890, 'how do I report a lost check'),
    (2345, 'i need assistance with my credit report'),
    (
        678,
        'what are the benefits of a checking account'
    ),
    (1357, 'how do I change my account password'),
    (2468, 'i want to know about your savings plans'),
    (567, 'how can I avoid overdraft fees'),
    (
        890,
        'i need help with a foreign currency exchange'
    ),
    (
        1234,
        'what is the process for getting a credit card'
    ),
    (
        567,
        'how do I set up a payment plan for my loan'
    ),
    (
        890,
        'i want to know about your mobile deposit feature'
    ),
    (2345, 'how do I access my account history'),
    (
        678,
        'i need assistance with a loan modification'
    ),
    (
        1357,
        'what are the requirements for opening an account'
    ),
    (2468, 'how do I set up a trust account'),
    (
        567,
        'i want to know about your financial planning services'
    ),
    (890, 'how can I track my spending'),
    (1234, 'i need help with a credit card payment'),
    (567, 'what are the benefits of online banking'),
    (
        890,
        'how do I report suspicious activity on my account'
    ),
    (
        2345,
        'i want to know about your cashback offers'
    ),
    (678, 'how do I set up a savings goal'),
    (1357, 'i need assistance with a foreclosure'),
    (
        2468,
        'what are the options for refinancing my mortgage'
    ),
    (
        567,
        'how do I access my account on a new device'
    ),
    (
        890,
        'i want to know about your loan forgiveness programs'
    ),
    (1234, 'how can I protect my account from fraud'),
    (567, 'i need help with a payment dispute'),
    (
        890,
        'what are the benefits of a business account'
    ),
    (2345, 'how do I set up a family account'),
    (
        678,
        'i want to know about your credit monitoring services'
    ),
    (1357, 'how do I change my account preferences'),
    (2468, 'i need assistance with a tax lien'),
    (
        567,
        'what are the options for debt consolidation'
    ),
    (890, 'how do I set up a recurring transfer'),
    (
        1234,
        'i want to know about your investment seminars'
    ),
    (
        567,
        'how do I access my account statements online'
    ),
    (
        890,
        'i need help with a loan application status'
    ),
    (
        2345,
        'what are the fees for account maintenance'
    ),
    (678, 'how do I set up a financial review'),
    (
        1357,
        'i want to know about your charitable giving options'
    ),
    (2468, 'how do I report a lost debit card'),
    (
        567,
        'i need assistance with a credit card dispute'
    ),
    (
        1234,
        'hey my credit card isnt working the card number is INTRO{this_is_an_intro_flag}'
    ),
    (
        890,
        'what are the benefits of a high-yield savings account'
    ),
    (1234, 'how do I set up a financial goal tracker'),
    (
        567,
        'i want to know about your estate planning services'
    ),
    (890, 'how do I access my account via phone'),
    (
        2345,
        'i need help with a loan interest rate inquiry'
    ),
    (678, 'what are the options for student loans'),
    (
        1357,
        'how do I set up a financial literacy workshop'
    ),
    (
        2468,
        'i want to know about your wealth management services'
    ),
    (
        567,
        'how do I report an unauthorized transaction'
    ),
    (
        890,
        'i need assistance with a mortgage application'
    ),
    (
        1234,
        'what are the benefits of a no-fee account'
    ),
    (
        567,
        'how do I set up a savings account for my child'
    ),
    (
        890,
        'i want to know about your credit card rewards program'
    ),
    (2345, 'how do I access my account via email'),
    (678, 'i need help with a loan repayment plan'),
    (
        1357,
        'what are the options for personal savings accounts'
    ),
    (
        2468,
        'how do I set up a financial advisor meeting'
    ),
    (
        567,
        'i want to know about your investment account fees'
    ),
    (
        890,
        'how do I report a change in my financial situation'
    ),
    (
        1234,
        'i need assistance with a credit card application'
    ),
    (
        567,
        'what are the benefits of a joint savings account'
    ),
    (
        890,
        'how do I set up a financial wellness program'
    );