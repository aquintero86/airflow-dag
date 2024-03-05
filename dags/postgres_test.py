from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime
from plugins.PostgresFileOperator import PostgresFileOperator

with DAG(
        dag_id = "mysql_dag",
        start_date= datetime(2024,2,25)

) as dag:
    task_1= PostgresOperator(postgres_conn_id="id_post",task_id="create_table",
                          sql= """ 
                            create table if not exists test_ml(
                            id varchar(100),
                            site_id varchar(100),
                            tittle  varchar(100),
                            price  varchar(100),
                            sold_quantity varchar(100),
                            thumbnail  varchar(200),
                            create_date varchar(10),
                            primary key (id, create_date)
                            )                  
                          """
            ),
    task_2= BashOperator(
        task_id="consult_API",
        bash_command="python /usr/local/airflow/plugins/temp/consult_api.py"
    ),
    task_3= PostgresFileOperator(
        task_id="insert_data",
        operation= "write",
        config= {"table_name" :"test_ml"}

    ),

    task_3= PostgresFileOperator(
        task_id="read_data",
        operation= "read",
        config= {"query" :"SELECT * from test_ml where sold_quantity != 'null' and (cast(sold_quantity as decimal)* cast(price as int)) > 4000000"}
    )
