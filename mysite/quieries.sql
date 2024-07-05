
SELECT "shopapp_product"."id", "shopapp_product"."name", "shopapp_product"."description", "shopapp_product"."price", "shopapp_product"."discount", "shopapp_product"."creted_at", "shopapp_product"."archived", "shopapp_product"."created_by_id", "shopapp_product"."preview"
FROM "shopapp_product"
WHERE NOT "shopapp_product"."archived"
ORDER BY "shopapp_product"."name" ASC, "shopapp_product"."price" ASC;

SELECT "django_session"."session_key", "django_session"."session_data", "django_session"."expire_date"
FROM "django_session"
WHERE ("django_session"."expire_date" > '2024-07-02 17:40:40.350920' AND "django_session"."session_key" = 'r53dw5lsjquobg843sccat29gcpr1lsi')
LIMIT 21;
('2024-07-02 17:40:40.350920', 'r53dw5lsjquobg843sccat29gcpr1lsi');

SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;



SELECT "shopapp_product"."id", "shopapp_product"."name", "shopapp_product"."description", "shopapp_product"."price", "shopapp_product"."discount", "shopapp_product"."creted_at", "shopapp_product"."archived", "shopapp_product"."created_by_id", "shopapp_product"."preview"
FROM "shopapp_product"
WHERE "shopapp_product"."id" = 10
LIMIT 21;
SELECT "shopapp_productimage"."id", "shopapp_productimage"."product_id", "shopapp_productimage"."image", "shopapp_productimage"."description"
FROM "shopapp_productimage"
WHERE "shopapp_productimage"."product_id" IN (10);

SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;



SELECT "django_session"."session_key", "django_session"."session_data", "django_session"."expire_date"
FROM "django_session"
WHERE ("django_session"."expire_date" > '2024-07-02 17:59:44.733732' AND "django_session"."session_key" = 'r53dw5lsjquobg843sccat29gcpr1lsi')
LIMIT 21;
('2024-07-02 17:59:44.733732', 'r53dw5lsjquobg843sccat29gcpr1lsi');
SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;
SELECT "shopapp_order"."id", "shopapp_order"."delivery_address", "shopapp_order"."promocode", "shopapp_order"."created_at", "shopapp_order"."user_id", "shopapp_order"."receipt", "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"
FROM "shopapp_order" INNER JOIN "auth_user" ON ("shopapp_order"."user_id" = "auth_user"."id");

SELECT ("shopapp_order_products"."order_id") AS "_prefetch_related_val_order_id", "shopapp_product"."id", "shopapp_product"."name", "shopapp_product"."description", "shopapp_product"."price", "shopapp_product"."discount", "shopapp_product"."creted_at", "shopapp_product"."archived", "shopapp_product"."created_by_id", "shopapp_product"."preview"
FROM "shopapp_product" INNER JOIN "shopapp_order_products" ON ("shopapp_product"."id" = "shopapp_order_products"."product_id")
WHERE "shopapp_order_products"."order_id" IN (2, 4, 5)
ORDER BY "shopapp_product"."name" ASC, "shopapp_product"."price" ASC;






SELECT "django_session"."session_key", "django_session"."session_data", "django_session"."expire_date"
FROM "django_session"
WHERE ("django_session"."expire_date" > '2024-07-02 18:08:26.472998' AND "django_session"."session_key" = 'r53dw5lsjquobg843sccat29gcpr1lsi')
LIMIT 21;
('2024-07-02 18:08:26.472998', 'r53dw5lsjquobg843sccat29gcpr1lsi');
SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;
SELECT "shopapp_order"."id", "shopapp_order"."delivery_address", "shopapp_order"."promocode", "shopapp_order"."created_at", "shopapp_order"."user_id", "shopapp_order"."receipt"
FROM "shopapp_order";

SELECT ("shopapp_order_products"."order_id") AS "_prefetch_related_val_order_id", "shopapp_product"."id", "shopapp_product"."name", "shopapp_product"."description", "shopapp_product"."price", "shopapp_product"."discount", "shopapp_product"."creted_at", "shopapp_product"."archived", "shopapp_product"."created_by_id", "shopapp_product"."preview"
FROM "shopapp_product" INNER JOIN "shopapp_order_products" ON ("shopapp_product"."id" = "shopapp_order_products"."product_id")
WHERE "shopapp_order_products"."order_id" IN (2, 4, 5)
ORDER BY "shopapp_product"."name" ASC, "shopapp_product"."price" ASC;

SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;
SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;
SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;




SELECT "django_session"."session_key", "django_session"."session_data", "django_session"."expire_date"
FROM "django_session"
WHERE ("django_session"."expire_date" > '2024-07-02 18:13:06.423285' AND "django_session"."session_key" = 'r53dw5lsjquobg843sccat29gcpr1lsi')
LIMIT 21; 
('2024-07-02 18:13:06.423285', 'r53dw5lsjquobg843sccat29gcpr1lsi');
SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21; 
SELECT "shopapp_order"."id", "shopapp_order"."delivery_address", "shopapp_order"."promocode", "shopapp_order"."created_at", "shopapp_order"."user_id", "shopapp_order"."receipt"
FROM "shopapp_order";

SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;
SELECT "shopapp_product"."id", "shopapp_product"."name", "shopapp_product"."description", "shopapp_product"."price", "shopapp_product"."discount", "shopapp_product"."creted_at", "shopapp_product"."archived", "shopapp_product"."created_by_id", "shopapp_product"."preview"
FROM "shopapp_product" INNER JOIN "shopapp_order_products" ON ("shopapp_product"."id" = "shopapp_order_products"."product_id")
WHERE "shopapp_order_products"."order_id" = 2
ORDER BY "shopapp_product"."name" ASC, "shopapp_product"."price" ASC;

SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21; 
SELECT "shopapp_product"."id", "shopapp_product"."name", "shopapp_product"."description", "shopapp_product"."price", "shopapp_product"."discount", "shopapp_product"."creted_at", "shopapp_product"."archived", "shopapp_product"."created_by_id", "shopapp_product"."preview"
FROM "shopapp_product" INNER JOIN "shopapp_order_products" ON ("shopapp_product"."id" = "shopapp_order_products"."product_id")
WHERE "shopapp_order_products"."order_id" = 4
ORDER BY "shopapp_product"."name" ASC, "shopapp_product"."price" ASC;

SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21; 
SELECT "shopapp_product"."id", "shopapp_product"."name", "shopapp_product"."description", "shopapp_product"."price", "shopapp_product"."discount", "shopapp_product"."creted_at", "shopapp_product"."archived", "shopapp_product"."created_by_id", "shopapp_product"."preview"
FROM "shopapp_product" INNER JOIN "shopapp_order_products" ON ("shopapp_product"."id" = "shopapp_order_products"."product_id")
WHERE "shopapp_order_products"."order_id" = 5
ORDER BY "shopapp_product"."name" ASC, "shopapp_product"."price" ASC;
