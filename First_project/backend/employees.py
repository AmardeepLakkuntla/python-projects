from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils import get_conn


router=APIRouter(tags=['Employees'])


# # ------------------------------------------------------------------------
# # |                    CREATE A NEW EMPLOYEE                           |
# # ------------------------------------------------------------------------

@router.post('/employees')
def create_employee(employee_id,name,position,region):
    conn=get_conn()
    cur=conn.cursor()
    query="INSERT INTO employees VALUES (%s,%s,%s,%s)"
    values=(employee_id,name,position,region)
    cur.execute(query,values)
    conn.commit()
    cur.close()
    conn.close()
    return {
        'message':'employee created successfully'
        }
    
    
# #  ------------------------------------------------
# #                   Read employees                |
# # -------------------------------------------------

@router.get('/employees')
def get_employees():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employees;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return JSONResponse(content=rows)


# # --------------------------------------------------------------------------
# # |                       READ EMPLYEE THROUGH EMP_ID                      |
# # --------------------------------------------------------------------------

@router.get('/employee/{emp_id}')
def get_employee_by_id(emp_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees WHERE employee_id=%s", (emp_id,))
    row = cur.fetchone()
    if not row:
        return JSONResponse(content={'msg': 'Employee Not found'})
    cur.close()
    conn.close()
    return JSONResponse(content=row)

# # -------------------------------------------------------------------------
# # |                       UPDATE AN EMPLOYEE                              |
# # -------------------------------------------------------------------------

@router.put("/employees/{employee_id}")
def update_employee(employee_id, name, position, region):
    conn = get_conn()
    cur = conn.cursor()
    query = "UPDATE employees SET name=%s, position=%s, region=%s WHERE employee_id=%s"
    values = (name, position, region, employee_id)
    cur.execute(query, values)
    conn.commit()
    cur.close()
    conn.close()
    return {"message": 'Employee updated'}

# # ------------------------------------------------------------------------------
# # |                       DELETE A EMPLOYEE                                    | 
# # ------------------------------------------------------------------------------

@router.delete("/employees/{employee_id}")
def delete_employee(employee_id):
    conn = get_conn()
    cur = conn.cursor()
    query = "DELETE FROM employees WHERE employee_id=%s;"
    values = (employee_id,)
    cur.execute(query, values)
    conn.commit()
    cur.close()
    conn.close()
    return {'message': 'Employee deleted successfully'}