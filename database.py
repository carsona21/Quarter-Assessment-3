import sqlite3

def create_tables():
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()

    # Create ACCT2110 table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ACCT2110 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT,
            option4 TEXT,
            correct_option INTEGER
        )
    ''')

    # Insert example questions for ACCT2110
    acct_questions = [
        ("What is the primary purpose of accounting?", "Recording transactions", "Managing personnel", "Developing software", "Analyzing competitors", 1),
        ("Which financial statement shows a company's assets and liabilities?", "Income Statement", "Balance Sheet", "Cash Flow Statement", "Statement of Equity", 2),
        ("What does GAAP stand for?", "General Accepted Accounting Principles", "Generally Applied Accounting Procedures", "Generally Accepted Accounting Principles", "Global Accounting and Auditing Policies", 3),
        ("Which account is considered a liability?", "Accounts Receivable", "Inventory", "Prepaid Rent", "Accounts Payable", 4),
        ("Depreciation is applied to which type of asset?", "Current Assets", "Intangible Assets", "Fixed Assets", "Inventory", 3),
        ("What is a journal entry in accounting?", "A summary of ledger balances", "An entry used to correct errors", "An entry recording financial transactions", "A budget forecast", 3),
        ("What is double-entry bookkeeping?", "Recording an entry twice", "Tracking profit and loss", "Entering two aspects of every transaction", "Auditing accounts twice a year", 3),
        ("Which of the following is an expense account?", "Cash", "Salaries Expense", "Accounts Receivable", "Notes Payable", 2),
        ("Revenue minus expenses equals?", "Net Income", "Gross Income", "Assets", "Liabilities", 1),
        ("Which of the following is considered a current asset?", "Land", "Buildings", "Cash", "Equipment", 3)
    ]

    cursor.executemany('''
        INSERT INTO ACCT2110 (question, option1, option2, option3, option4, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', acct_questions)

    # Create BMGT3500 table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS BMGT3500 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT,
            option4 TEXT,
            correct_option INTEGER
        )
    ''')

    # Insert example questions for BMGT3500
    bmgt_questions = [
        ("What is management?", "Overseeing and coordinating activities", "Developing software systems", "Executing financial transactions", "Building structures", 1),
        ("Which of the following is a function of management?", "Planning", "Programming", "Sketching", "Acting", 1),
        ("What does SWOT analysis stand for?", "Strategy, Workforce, Organization, Tasks", "Strengths, Weaknesses, Opportunities, Threats", "Sales, Warehouse, Operations, Technology", "Services, Waste, Options, Tools", 2),
        ("Which leadership style involves high control over employees?", "Autocratic", "Democratic", "Laissez-faire", "Participative", 1),
        ("What is organizational culture?", "Formal written rules", "Shared values, beliefs, and norms", "The number of employees in an organization", "Management's salary", 2),
        ("What is the primary goal of strategic planning?", "To ensure day-to-day operations", "To create long-term objectives and goals", "To manage equipment", "To prepare financial statements", 2),
        ("What is a mission statement?", "A company's financial report", "A detailed workflow plan", "A declaration of purpose", "An employee evaluation", 3),
        ("Which of the following is a motivation theory?", "Maslow's Hierarchy of Needs", "Ohm's Law", "Newton's Third Law", "Theory of Relativity", 1),
        ("Effective communication in management involves?", "Only sending messages", "Sending and receiving messages effectively", "Recording all activities", "Completing tasks alone", 2),
        ("Which type of planning focuses on short-term activities?", "Operational planning", "Strategic planning", "Contingency planning", "Leadership planning", 1)
    ]

    cursor.executemany('''
        INSERT INTO BMGT3500 (question, option1, option2, option3, option4, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', bmgt_questions)

    # Create ECON4900 table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ECON4900 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT,
            option4 TEXT,
            correct_option INTEGER
        )
    ''')

    # Insert example questions for ECON4900
    econ_questions = [
        ("What is economics primarily concerned with?", "The production and distribution of resources", "The study of plant life", "The art of cooking", "The development of software", 1),
        ("What is opportunity cost?", "The cost of a lost opportunity", "The cost of making a choice", "The additional gain from a decision", "A cost incurred by chance", 2),
        ("Which of these is a macroeconomic indicator?", "Interest rates", "A company's sales report", "Employee performance", "A single factory's output", 1),
        ("What does GDP stand for?", "Global Domestic Product", "Gross Domestic Product", "General Department of Policy", "Grand Data Plan", 2),
        ("What is supply and demand?", "A political theory", "The relationship between prices and quantities available", "The study of human behavior", "A legal framework for contracts", 2),
        ("What is a monopoly?", "A company with exclusive control over a market", "An agreement between two parties", "A type of partnership", "A form of capital investment", 1),
        ("Who is considered the father of modern economics?", "Albert Einstein", "Adam Smith", "Isaac Newton", "Henry Ford", 2),
        ("What is inflation?", "A decrease in the money supply", "An increase in the general level of prices", "The fluctuation of interest rates", "A decrease in consumer spending", 2),
        ("Which branch of economics focuses on individual behavior?", "Microeconomics", "Macroeconomics", "Metaeconomics", "Geoeconomics", 1),
        ("What is fiscal policy?", "Government adjustment of spending levels and tax rates", "Central bank control of the money supply", "Policies relating to foreign trade", "Rules for corporate governance", 1)
    ]

    cursor.executemany('''
        INSERT INTO ECON4900 (question, option1, option2, option3, option4, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', econ_questions)

    # Create MKT3400 table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS MKT3400 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT,
            option4 TEXT,
            correct_option INTEGER
        )
    ''')

    # Insert example questions for MKT3400
    mkt_questions = [
        ("What is marketing?", "The process of creating value and building relationships with customers", "The production of goods", "The study of financial markets", "The management of human resources", 1),
        ("What is a market segment?", "A group of consumers with similar needs", "A company's total revenue", "An advertising strategy", "A competitor's market share", 1),
        ("What is the 4Ps model in marketing?", "Product, Price, Place, Promotion", "People, Places, Plans, Profits", "Processes, People, Plants, Products", "Policies, Promotions, Pricing, Performance", 1),
        ("Which of the following is a pricing strategy?", "Penetration pricing", "Laissez-faire pricing", "Balanced scorecard pricing", "Ethical pricing", 1),
        ("What does a brand represent?", "A company's financial statement", "The total experience and perception of a product", "An employee policy handbook", "The physical location of a company", 2),
        ("What is the primary goal of advertising?", "To inform and persuade consumers", "To minimize operational costs", "To develop product prototypes", "To create legal frameworks", 1),
        ("What is a distribution channel?", "A path through which goods and services travel from the producer to the consumer", "A type of investment vehicle", "A way to optimize office layouts", "A method for reducing taxes", 1),
        ("What is consumer behavior?", "The study of how individuals make purchasing decisions", "The process of product production", "The study of supply chain logistics", "A focus on employee management", 1),
        ("Which of the following is a promotional tool?", "Advertising", "Supply chain integration", "Inventory control", "Tax compliance", 1),
        ("What is market research?", "Gathering information about consumers and markets to support business decisions", "A regulatory process", "An investment strategy", "A method of accounting", 1)
    ]

    cursor.executemany('''
        INSERT INTO MKT3400 (question, option1, option2, option3, option4, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', mkt_questions)

    # Create FIN3210 table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS FIN3210 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT,
            option4 TEXT,
            correct_option INTEGER
        )
    ''')

    # Insert example questions for FIN3210
    fin3210_questions = [
        ("What is the primary focus of corporate finance?", "Maximizing shareholder value", "Minimizing employee turnover", "Developing new products", "Complying with regulations", 1),
        ("What is the purpose of capital budgeting?", "Determining the long-term profitability of investments", "Calculating daily sales", "Monitoring employee productivity", "Managing short-term cash flows", 1),
        ("Which of the following is a financial instrument?", "A stock", "A factory", "A computer", "An employee contract", 1),
        ("What is the time value of money?", "A principle that money available now is worth more than the same amount in the future due to its earning capacity", "A rule for accounting entries", "A method for calculating taxes", "A technique for inventory management", 1),
        ("Which ratio measures a firm's liquidity?", "Current ratio", "Debt ratio", "Profit margin", "Inventory turnover", 1),
        ("What is financial leverage?", "The use of debt to increase the potential return on investment", "A marketing strategy", "The process of hiring employees", "A method for inventory control", 1),
        ("What is risk diversification?", "Spreading investments across different assets to reduce risk", "Placing all investments in one stock", "Selling assets at a loss", "None of the above", 1),
        ("Which of the following is a bond valuation method?", "Present value of cash flows", "Market segmentation", "Customer satisfaction survey", "Employee appraisal", 1),
        ("What is a common stock?", "A type of security that represents ownership in a corporation", "A government bond", "A fixed-income asset", "An inventory item", 1),
        ("What is net present value (NPV)?", "The difference between the present value of cash inflows and outflows over a period of time", "A method of calculating taxes", "A management style", "An HR policy", 1)
    ]

    cursor.executemany('''
        INSERT INTO FIN3210 (question, option1, option2, option3, option4, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', fin3210_questions)

    conn.commit()
    conn.close()

create_tables()
