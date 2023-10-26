from flask import Flask, Blueprint, jsonify, request
import os
import psycopg2

app = Flask(__name__)

bp = Blueprint("api", __name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='ailabpostgres.postgres.database.azure.com',
        database='stagiaires',
        user=os.environ.get('DB_USER', 'fatma.aljane.1@ens.etsmtl.ca'),
        password=os.environ.get('DB_PASSWORD', 'H1T 1M5')
    )
    return conn

@bp.route('/api', methods=['GET'])
def get_top_n():
    
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                SELECT crawl_view.*, score_view.score 
                FROM crawl_view 
                JOIN score_view ON crawl_view.id = score_view.entity_id
                ORDER BY score_view.score DESC''')
            
            rows = cur.fetchall()
            

    return jsonify(rows)


if __name__ == '__main__':
    app.run(debug=True)
