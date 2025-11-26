import psycopg2
 
DB_URL = 'postgresql://postgres.ljpnrtyazmqrcdqvsyrq:123456789@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres'
 
def get_conn():
    conn = psycopg2.connect(DB_URL)
    return conn