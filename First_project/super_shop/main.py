import streamlit as st
import requests
 
 
 
 
               
  #---------------------------------------------------------------------------------------------------
  #                                          "EMPLOYEES"
  #---------------------------------------------------------------------------------------------------
 
 
# CREATE EMPLOYEEES
@st.dialog('Create Employee')
def create_employee_dialog():
    emp_id = st.number_input("Enter Emp ID", min_value=1)
    emp_name = st.text_input("Enter Name")
    emp_position = st.selectbox("Select Position", ['Manager', 'Cashier', 'Waiter'])
    emp_region = st.selectbox("Select region", ['North', 'South'])
    create_btn = st.button("Create Employee", type='primary')
    if create_btn:
        url = f"http://127.0.0.1:8000/employees?employee_id={emp_id}&name={emp_name}&position={emp_position}&region={emp_region}"
        res = requests.post(url)
        if res.status_code == 200:
            st.toast("Employee created successfully")
            st.rerun()
 
 # UPDATE EMPLOYEES
 
@st.dialog('Update Employee')
def update_employee_dialog():
    emp_id = st.number_input("Enter Emp ID", min_value=1)
    emp_name = st.text_input("Enter Name")
    emp_position = st.selectbox("Select Position", ['Manager', 'Cashier', 'Waiter'])
    emp_region = st.selectbox("Select region", ['North', 'South'])
    #data= {'employee_id' : emp_id,'name' : emp_name,'position' : emp_position, 'region' : emp_region}
    update_btn = st.button("Update Employee", type='primary')
    if update_btn:
        # url = f"http://127.0.0.1:8000/employees?employee_id={emp_id}&name={emp_name}&position={emp_position…
        url = f"http://127.0.0.1:8000/employees/{emp_id}?name={emp_name}&position={emp_position}&region={emp_region}"
 
        res = requests.put(url)
        if res.status_code == 200:
            st.toast("Employee Updated successfully")
            st.rerun()
           
           
# DELETE EMPLOYEES
 
@st.dialog('Delete Employee')
def delete_employee_dialog():
    emp_id = st.number_input("Enter Emp ID", min_value=1)
    delete_btn = st.button("Delete Employee", type='primary')
    if delete_btn:
        # url = f"http://127.0.0.1:8000/employees?employee_id={emp_id}"
        url = f"http://127.0.0.1:8000/employees/{emp_id}"
 
       
        res = requests.delete(url)
        if res.status_code == 200:
            st.toast("Employee Deleted successfully")
            st.rerun()
 
 
 
st.header('SuperShop')
tabs = st.tabs(['Employees', 'Products','Sales'])
with tabs[0]:
    col1, col2, col3 = st.columns([1,1,1])
 
with col1:
    button1 = st.button("Create" , type= "primary")
    # create_employee_dialog()
    if button1:
          create_employee_dialog()
    res = requests.get("http://127.0.0.1:8000/employees")
    if res.status_code == 200:
        res = res.json()
        for employee in res:
            with st.container(border=True):
                st.subheader(employee[1])
                st.write(f"Emp_ID : {employee[0]}")
                st.write(employee[2] + " | " + employee[3])
 
 
 
with col2:
    button2 = st.button("Update", type="primary")
    if button2:
        update_employee_dialog()
 
 
with col3:
    button3 = st.button("Delete", type="primary")
    if button3:
        delete_employee_dialog()
   
   
               
               
  #---------------------------------------------------------------------------------------------------
  #                                          "PRODUCTS"
  #---------------------------------------------------------------------------------------------------
 
  #CREATE PRODUCTS
               
@st.dialog('Create Products')
def create_product_dialog():
    product_id = st.number_input("Enter Product ID", min_value=1)
    product_name = st.text_input("Enter Name")
    product_category = st.selectbox("Select product", ['Healthy', 'Fast Food','Drinks'])
    product_price = st.number_input("Enter price", min_value = 100)
    create_btn = st.button("Create Products", type='primary')
    if create_btn:
        url = f"http://127.0.0.1:8000/products?product_id={product_id}&product_name={product_name}&category={product_category}&price={product_price}"
        res = requests.post(url)
        if res.status_code == 200:
            st.toast("Product created successfully")
            st.rerun()    
           
           
 #UPDATE PRODUCTS          
               
@st.dialog('Update Products')
def update_product_dialog():
    product_id = st.number_input("Enter Product ID", min_value=1)
    product_name = st.text_input("Enter Name")
    product_category = st.selectbox("Select product", ['Healthy', 'Fast Food','Drinks'])
    product_price = st.number_input("Enter price", min_value = 100)
    create_btn = st.button("Update Products", type='primary', key = update_product_dialog)
    if create_btn:
        #url = f"http://127.0.0.1:8000/products/{product_id}?products_name={product_name}&category={product_cate…
        url = f"http://127.0.0.1:8000/products/{product_id}?product_name={product_name}&category={product_category}&price={product_price}"
 
        res = requests.put(url)
        if res.status_code == 200:
            st.toast("Product Updated successfully")
            st.rerun()  
           
           
#DELETE PRODUCTS          
 
@st.dialog('Delete Products')
def delete_product_dialog():
    product_id = st.number_input("Enter Product ID", min_value=1)
   
    create_btn = st.button("Delete Products", type='primary',key=delete_product_dialog)
    if create_btn:
        # url = f"http://127.0.0.1:8000/products/{product_id}"
        url = f"http://127.0.0.1:8000/products/{product_id}"
 
        res = requests.delete(url)
        if res.status_code == 200:
            st.toast("Product Deleted successfully")
            st.rerun()              
with tabs[1]:
    col1, col2, col3 = st.columns([1,1,1])            
 
    with col1:
            button1 = st.button('Create ', type= 'primary' )
            if button1:
                create_product_dialog()
            res = requests.get("http://127.0.0.1:8000/products")
            if res.status_code == 200:
                res = res.json()
                for products in res:
                    with st.container(border=True):
                        st.subheader(products[1])
                        st.write(products[2] + " | RS." + str(products[3]))
                       
    with col2:
            button2 = st.button('Update', type='primary',key='update_product')
            if button2 :
                update_product_dialog()
               
    with col3:
            button3 = st.button('Delete', type='primary',key='delete_product')
            if button3 :
                delete_product_dialog()
       
 
               
               
 
 
               
  #---------------------------------------------------------------------------------------------------
  #                                          "SALES"
  #---------------------------------------------------------------------------------------------------
 
 
 
                             
 #CREATE SALES
               
@st.dialog('Create sale')
def create_sale_dialog():
    sale_id = st.number_input("Enter Product ID", min_value=1)
    sale_date = st.date_input("Enter Date",format="YYYY-MM-DD")
    employee_id = st.number_input("Select employee Id", min_value=1)
    product_id = st.number_input("Enter product Id", min_value = 1)
    quantity = st.number_input("Enter Quantity", min_value = 1)
    total_amount =st.number_input("Enter Total Amount ",min_value=100 )
    create_btn = st.button("Create sale", type='primary',key=create_sale_dialog)
    if create_btn:
        url = f"http://127.0.0.1:8000/sales?sale_id={sale_id}&sale_date={sale_date}&employee_id={employee_id}&product_id={product_id}&quantity={quantity}&total_amount={total_amount}"
        res = requests.post(url)
        if res.status_code == 200:
            st.toast("Sale created successfully")
            st.rerun()                
               
               
#UPDATE SALES
               
@st.dialog('Update sale')
def update_sale_dialog():
    sale_id = st.number_input("Enter Sale ID", min_value=1)
    sale_date = st.date_input("Enter Date",format="YYYY-MM-DD")
    employee_id = st.number_input("Select employee Id", min_value=1)
    product_id = st.number_input("Enter product Id", min_value = 1)
    quantity = st.number_input("Enter Quantity", min_value = 1)
    total_amount =st.number_input("Enter Total Amount ",min_value=100 )
    update_btn = st.button("Update sale", type='primary',key=update_sale_dialog)
    if update_btn:
        url = f"http://127.0.0.1:8000/sales/{sale_id}?sale_date={sale_date}&employee_id={employee_id}&product_id={product_id}&quantity={quantity}&total_amount={total_amount}"
        res = requests.put(url)
        if res.status_code == 200:
            st.toast("Sale update successfully")
            st.rerun()      
           
           
  #DELETE SALES          
 
               
@st.dialog('Delete sale')
def delete_sale_dialog():
    sale_id = st.number_input("Enter Sale ID", min_value=1)
   
    delete_btn = st.button("Delete sale", type='primary',key=delete_sale_dialog)
    if delete_btn:
        url = f"http://127.0.0.1:8000/sales/{sale_id}"
        res = requests.delete(url)
        if res.status_code == 200:
            st.toast("Sale delete successfully")
            st.rerun()      
 
with tabs[2]:
    col1,col2,col3 = st.columns([1,1,1])
    with col1:
      button1 = st.button('Create ',type="primary",key="create_sale")
    if button1:
        create_sale_dialog()    
    res = requests.get("http://127.0.0.1:8000/sales")
    if res.status_code == 200:
        res = res.json()
        for sales in res:
            with st.container(border=True):
                st.subheader(f"Sale ID {sales[0]}")
                st.write(f"DATE {sales[1]}" )
                st.write(f"Emp_Id {sales[2]}")
                st.write(f"Product_Id {sales[3]}")
                st.write(f"Quantity {sales[4]}")
                st.write(f"Total Amount {sales[5]}")
               
    with col2:
        button2=st.button('update',type="primary",key="update_sale")
        if button2:
            update_sale_dialog()
           
    with col3:
        button3=st.button('Delete',type="primary",key="delete_sale")
        if button3:
            delete_sale_dialog()
            
            
