from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from employees import router as employee_router
from products import router as products_router
from sales import router as sales_router
 
 
app = FastAPI()
app.include_router(employee_router)
app.include_router(products_router)
app.include_router(sales_router)
 












# from fastapi import FastAPI
# from fastapi.responses import JSONResponse
# import psycopg2
# from psycopg2.extras import RealDictCursor
 
# app = FastAPI()
 
 
# DB_URL = 'postgresql://postgres.ljpnrtyazmqrcdqvsyrq:123456789@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres'
 
# def get_conn():
#     conn = psycopg2.connect(DB_URL)
#     return conn
 
# #  ------------------------------------------------
# #              1.1  Read employees                |
# # -------------------------------------------------

# # -------------------------------------------------

# @app.get('/employees')
# def get_employees():
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM employees;')
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return JSONResponse(content=rows)

# # --------------------------------------------------

# # --------------------------------------------------------------------------
# # |                   1.2 READ EMPLYEE THROUGH EMP_ID                      |
# # --------------------------------------------------------------------------

# # -------------------------------------------------------------------------
 
# @app.get('/employee/{emp_id}')
# def get_employee_by_id(emp_id):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM employees WHERE employee_id=%s", (emp_id,))
#     row = cur.fetchone()
#     if not row:
#         return JSONResponse(content={'msg': 'Employee Not found'})
#     cur.close()
#     conn.close()
#     return JSONResponse(content=row)
# # ---------------------------------------------------------------------------

# # ----------------------------------------------------
# # |              1.2 READ PRODUCTS                    |
# # ----------------------------------------------------

# # ------------------------------------------------------

# @app.get('/products')
# def get_products():
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM products;')
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return JSONResponse(content=rows)

# # --------------------------------------------------------

# # ---------------------------------------------------------------------------
# # |                   1.21  READ PRODUCT THROUGH PROD_ID                    |
# # ---------------------------------------------------------------------------

# # ----------------------------------------------------------------------------

# @app.get('/product/{product_id}')
# def get_product_by_id(product_id):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM products WHERE product_id=%s", (product_id,))
#     row = cur.fetchone()
#     if not row:
#         return JSONResponse(content={'msg': 'product Not found'})
#     cur.close()
#     conn.close()
#     return JSONResponse(content=row)

# # ------------------------------------------------------------------------------

# # -------------------------------------------------------
# # |                 1.3  READ SALES                     |
# # -------------------------------------------------------

# # ----------------------------------------------------

# @app.get('/sales')
# def get_sales():
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM sales;')
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return rows

# # -------------------------------------------------

# # ---------------------------------------------------------------------
# #             1.3  READ SALES THROUGH SALE_ID                          |
# # ---------------------------------------------------------------------

# @app.get('/sale/{sale_id}')
# def get_sale_by_id(sale_id):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM sales WHERE sale_id=%s", (sale_id,))
#     row = cur.fetchone()
#     if not row:
#         return JSONResponse(content={'msg': 'sale Not found'})
#     cur.close()
#     conn.close()
#     return row

# # -----------------------------------------------------------------------------



# # ------------------------------------------------------------------------
# # |                  2.1  CREATE A NEW EMPLOYEE                           |
# # ------------------------------------------------------------------------

# # -----------------------------------------------------------------------

# @app.post('/employees')
# def create_employee(employee_id,name,position,region):
#     conn=get_conn()
#     cur=conn.cursor()
#     query="INSERT INTO employees VALUES (%s,%s,%s,%s)"
#     values=(employee_id,name,position,region)
#     cur.execute(query,values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return {
#         'message':'employee created successfully'
#         }
    
# # --------------------------------------------------------------------

# # --------------------------------------------------------------------
# #                    2.2 CREATE A NEW PRODUCT                        |
# # --------------------------------------------------------------------

# # --------------------------------------------------------------------
# @app.post('/products')
# def create_product(product_id,product_name,category,price):
#     conn=get_conn()
#     cur=conn.cursor()
#     query="INSERT INTO products VALUES (%s,%s,%s,%s)"
#     values=(product_id,product_name,category,price)
#     cur.execute(query,values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return {
#         'message':'product created successfully'
#         }
    
# # ----------------------------------------------------------------------

# # ----------------------------------------------------------------------
# # |                   2.3 CREATE A NEW SALE                            |
# # ----------------------------------------------------------------------

# # ----------------------------------------------------------------------
# @app.post('/sales')
# def create_sales(sale_id,sale_date,product_id,employee_id,quantity,total_amount):
#     conn = get_conn()
#     cur = conn.cursor()
#     query="INSERT into SALES VALUES (%s,%s,%s,%s,%s,%s)"
#     values=(sale_id,sale_date,product_id,employee_id,quantity,total_amount)
#     cur.execute(query,values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return {
#          'message':'sale created successfully'
#     }
    
# # -------------------------------------------------------------------------


# # -------------------------------------------------------------------------


# # -------------------------------------------------------------------------
# # |                   3.1  UPDATE AN EMPLOYEE                              |
# # -------------------------------------------------------------------------

# # -------------------------------------------------------------------------

# @app.put("/employees/{employee_id}")
# def update_employee(employee_id, name, position, region):
#     conn = get_conn()
#     cur = conn.cursor()
#     query = "UPDATE employees SET name=%s, position=%s, region=%s WHERE employee_id=%s"
#     values = (name, position, region, employee_id)
#     cur.execute(query, values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return {"message": 'Employee updated'}
    
#     # -------------------------------------------------------------------------------
    
#     # --------------------------------------------------------------------------------
#     # |                      3.2 UPDATE A PRODUCT                                    |
#     # --------------------------------------------------------------------------------
    
#     # --------------------------------------------------------------------------------
    
# @app.put("/products/{product_id}")
# def update_product(product_id,product_name,category,price):
#     conn=get_conn()
#     cur=conn.cursor()
#     query="UPDATE products SET product_name=%s,category=%s,price=%s WHERE product_id=%s"
#     values=(product_name,category,price,product_id)
#     cur.execute(query,values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return{
#         'message':'product updated'
#     }
    
# # --------------------------------------------------------------------------


# # ----------------------------------------------------------------------------

# # ----------------------------------------------------------------------------
# # |                         3.3 UPDATE A SALE                                |
# # ----------------------------------------------------------------------------

# # ----------------------------------------------------------------------------

# @app.put("/sales/{sale_id}")
# def update_sale(sale_id,sale_date,product_id,emp_id,quantity,total_amount):
#     conn=get_conn()
#     cur=conn.cursor()
#     query="UPDATE sales SET sale_date=%s,product_id=%s,emp_id=%s,quantity=%s,total_amount WHERE sale_id=%s"
#     values=(sale_date,product_id,emp_id,quantity,total_amount,sale_id)
#     cur.execute(query,values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return{
#         'message':'sale updated'
#     }
    
# # ------------------------------------------------------------------------------------------------------------


# # ------------------------------------------------------------------------------------------------------------

# # -----------------------------------------------------------------------------------------------
# # |                                    4.1 DELETE A EMPLOYEE                                    | 
# # -----------------------------------------------------------------------------------------------

# # ------------------------------------------------------------------------------------------------------------
    
# @app.delete("/employees/{employee_id}")
# def delete_employee(employee_id):
#     conn = get_conn()
#     cur = conn.cursor()
#     query = "DELETE FROM employees WHERE employee_id=%s;"
#     values = (employee_id,)
#     cur.execute(query, values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return {'message': 'Employee deleted successfully'}

#     # ----------------------------------------------------------------------------------------
    
    
#     # ----------------------------------------------------------------------------------------
#     # |                         4.2 DELETE A PRODUCT                                         |
#     # -----------------------------------------------------------------------------------------
    
#     # -----------------------------------------------------------------------------------------
    
# @app.delete("/products/{product_id}")
# def delete_product(product_id):
#     conn = get_conn()
#     cur = conn.cursor()
#     query = "DELETE FROM products WHERE product_id=%s;"
#     values = (product_id,)
#     cur.execute(query, values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return {'message': 'product deleted successfully'}

# # @app.delete("/products/{products_id}")
# # def delete_product(products_id):
# #     conn = get_conn()
# #     cur = conn.cursor()
# #     query = " DELETE FROM products WHERE products_id =%s"
# #     values = (products_id,)
# #     cur.execute(query,values)
# #     conn.commit()
# #     cur.close()
# #     conn.close()
# #     return{"Message" : "Deleted successfull"}




    
# # --------------------------------------------------------------------------------------


# # --------------------------------------------------------------------------------------
# # |                           3.3 DELETE A SALE                                        |
# # --------------------------------------------------------------------------------------

# # --------------------------------------------------------------------------------------

# @app.delete("/sales/{sale_id}")
# def delete_sale(sale_id):
#     conn=get_conn()
#     cur=conn.cursor()
#     query="DELETE FROM sales  WHERE sale_id=%s"
#     values=(sale_id,)
#     cur.execute(query,values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return{
#         'message':'sale deleted'
#     }
    
    


 
# #2. Create a new employee
# #3. Update an employee
# #4. Delete an employee
 