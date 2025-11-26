from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils import get_conn


router=APIRouter(tags=['Sales'])


# # ----------------------------------------------------------------------
# # |                       CREATE A NEW SALE                            |
# # ----------------------------------------------------------------------

@router.post('/sales')
def create_sales(sale_id,sale_date,product_id,employee_id,quantity,total_amount):
    conn = get_conn()
    cur = conn.cursor()
    query="INSERT into SALES VALUES (%s,%s,%s,%s,%s,%s)"
    values=(sale_id,sale_date,product_id,employee_id,quantity,total_amount)
    cur.execute(query,values)
    conn.commit()
    cur.close()
    conn.close()
    return {
         'message':'sale created successfully'
    }
    

# # -------------------------------------------------------
# # |                      READ SALES                     |
# # -------------------------------------------------------


@router.get('/sales')
def get_sales():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM sales;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


# # ---------------------------------------------------------------------
# #                 READ SALES THROUGH SALE_ID                          |
# # ---------------------------------------------------------------------

@router.get('/sale/{sale_id}')
def get_sale_by_id(sale_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM sales WHERE sale_id=%s", (sale_id,))
    row = cur.fetchone()
    if not row:
        return JSONResponse(content={'msg': 'sale Not found'})
    cur.close()
    conn.close()
    return row

# # ----------------------------------------------------------------------------
# # |                             UPDATE A SALE                                |
# # ----------------------------------------------------------------------------

@router.put("/sales/{sale_id}")
def update_sale(sale_id,sale_date,product_id,employee_id,quantity,total_amount):
    conn=get_conn()
    cur=conn.cursor()
    query="UPDATE sales SET sale_date=%s,product_id=%s,employee_id=%s,quantity=%s,total_amount=%s WHERE sale_id=%s"
    values=(sale_date,product_id,employee_id,quantity,total_amount,sale_id)
    cur.execute(query, values)
    conn.commit()
    cur.close()
    conn.close()
    return{
        'message':'sale updated'
    }


# # --------------------------------------------------------------------------------------
# # |                               DELETE A SALE                                        |
# # --------------------------------------------------------------------------------------

@router.delete("/sales/{sale_id}")
def delete_sale(sale_id):
    conn=get_conn()
    cur=conn.cursor()
    query="DELETE FROM sales  WHERE sale_id=%s"
    values=(sale_id,)
    cur.execute(query,values)
    conn.commit()
    cur.close()
    conn.close()
    return{
        'message':'sale deleted'
    }