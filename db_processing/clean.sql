DELETE FROM scin_pub_figure
 WHERE doc_id NOT IN (SELECT F.doc_id
                        FROM pub_tech_prod_result F);

DELETE FROM scin_pub_material_n_method
 WHERE doc_id NOT IN (SELECT F.doc_id
                        FROM pub_tech_prod_result F);

DELETE FROM scin_pub_result
 WHERE doc_id NOT IN (SELECT F.doc_id
                        FROM pub_tech_prod_result F);

DELETE FROM scin_pub_support_info
 WHERE doc_id NOT IN (SELECT F.doc_id
                        FROM pub_tech_prod_result F);

DELETE FROM pub_supplier_result
 WHERE doc_id NOT IN (SELECT F.doc_id
                        FROM pub_tech_prod_result F);

DELETE FROM pub_product_result
 WHERE doc_id NOT IN (SELECT F.doc_id
                        FROM pub_tech_prod_result F);

DELETE FROM scin_pub_meta
 WHERE id NOT IN (SELECT F.doc_id
                        FROM pub_tech_prod_result F);

DELETE FROM pub_product_name
 WHERE prod_id NOT IN (SELECT F.prod_id
                        FROM pub_tech_prod_result f);

DELETE FROM pub_product_result
 WHERE prod_id NOT IN (SELECT F.prod_id
                        FROM pub_tech_prod_result f);

 DELETE FROM pub_product_info
 WHERE id NOT IN (SELECT F.prod_id
                        FROM pub_tech_prod_result f);