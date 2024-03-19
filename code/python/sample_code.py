from jira import JIRA
import logging

# Fibonacci Series Function
def fibonacci(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Configure Jira 
jira = JIRA(server="https://yourjira.atlassian.net", basic_auth=("username", "password"))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define Confluence parameters
confluence_space_name = 'TEST'
parent_page_title = 'Fibonacci Series'
page_title = 'Fibo_Results'

# Generate Fibonacci series
series = [str(fibonacci(x)) for x in range(0, 10)]  

# Create/Update confluence page
page = jira.confluence.get_page_by_title(space=confluence_space_name, title=page_title)
if page:
    logger.info('Updating page')
    jira.confluence.update_page(
        parent_id=page.get('id'),
        page_id=page.get('id'),
        title=page_title, 
        body='\n'.join(series),
        type='page',
        space=confluence_space_name
    )
else:
    logger.info('Creating new page') 
    jira.confluence.create_page(
        space=confluence_space_name,
        parent_id=jira.confluence.get_page_id(confluence_space_name, parent_page_title),
        title=page_title,
        body='\n'.join(series)
   )

logger.info('Done')
