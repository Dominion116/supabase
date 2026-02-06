from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL=os.getenv('SUPABASE_URL')
SUPABASE_KEY=os.getenv('SUPABASE_KEY')

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# new_row = {"first_name": "Jane"}
# supabase.table('demo-table').update(new_row).eq('id', 2).execute()

# supabase.table('demo-table').delete().eq('id', 2).execute()

supabase.storage.from_('demo-bucket').upload('hello.txt', 'Hello, World!')

results = supabase.table('demo-table').select('*').execute()
print(results)
