from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils import get_conn


router=APIRouter(tags=['Products'])


# # --------------------------------------------------------------------
# #                        CREATE A NEW PRODUCT                        |
# # --------------------------------------------------------------------

@router.post('/products')
def create_product(product_id,product_name,category,price):
    conn=get_conn()
    cur=conn.cursor()
    query="INSERT INTO products VALUES (%s,%s,%s,%s)"
    values=(product_id,product_name,category,price)
    cur.execute(query,values)
    conn.commit()
    cur.close()
    conn.close()
    return {
        'message':'product created successfully'
        }
    
# # ----------------------------------------------------
# # |                 READ PRODUCTS                    |
# # ----------------------------------------------------

@router.get('/products')
def get_products():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM products;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return JSONResponse(content=rows)

# # ---------------------------------------------------------------------------
# # |                         READ PRODUCT THROUGH PROD_ID                    |
# # ---------------------------------------------------------------------------

@router.get('/product/{product_id}')
def get_product_by_id(product_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE product_id=%s", (product_id,))
    row = cur.fetchone()
    if not row:
        return JSONResponse(content={'msg': 'product Not found'})
    cur.close()
    conn.close()
    return JSONResponse(content=row)

#     # --------------------------------------------------------------------------------
#     # |                           UPDATE A PRODUCT                                    |
#     # --------------------------------------------------------------------------------

@router.put("/products/{product_id}")
def update_product(product_id,product_name,category,price):
    conn=get_conn()
    cur=conn.cursor()
    query="UPDATE products SET product_name=%s,category=%s,price=%s WHERE product_id=%s"
    values=(product_name,category,price,product_id)
    cur.execute(query,values)
    conn.commit()
    cur.close()
    conn.close()
    return{
        'message':'product updated'
    }
    

#     # ----------------------------------------------------------------------------------------
#     # |                             DELETE A PRODUCT                                         |
#     # ----------------------------------------------------------------------------------------
    

@router.delete("/products/{product_id}")
def delete_product(product_id):
    conn = get_conn()
    cur = conn.cursor()
    query = "DELETE FROM products WHERE product_id=%s;"
    values = (product_id,)
    cur.execute(query, values)
    conn.commit()
    cur.close()
    conn.close()
    return {'message': 'product deleted successfully'}




