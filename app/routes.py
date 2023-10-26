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

@bp.route('/topn', methods=['GET'])
def get_top_n():
    top_n = request.args.get('n', type=int, default=10)
    
    # Valider que topN est entre 1 et 100
    if not 1 <= top_n <= 100:
        return jsonify({"error": "Parameter n should be between 1 and 100"}), 400
    
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                SELECT crawl_view.*, score_view.score 
                FROM crawl_view 
                JOIN score_view ON crawl_view.id = score_view.entity_id
                ORDER BY score_view.score DESC
                LIMIT %s
            ''', (top_n,))
            
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            result = [dict(zip(columns, row)) for row in rows]

    return jsonify(result)

app.register_blueprint(bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
 