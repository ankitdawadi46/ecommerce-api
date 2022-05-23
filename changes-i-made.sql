BEGIN;
--
-- Add field user to reviewproducts
--
ALTER TABLE "products_reviewproducts" ADD COLUMN "user_id" bigint NULL CONSTRAINT "products_reviewproducts_user_id_4e2de819_fk_user_user_id" REFERENCES "user_user"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_reviewproducts_user_id_4e2de819_fk_user_user_id" IMMEDIATE;
--
-- Add field products_combinations_id to products_stocks
--
ALTER TABLE "products_products_stocks" ADD COLUMN "products_combinations_id_id" bigint NOT NULL CONSTRAINT "products_products_st_products_combination_90fce356_fk_products_" REFERENCES "products_products_combinations"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_products_st_products_combination_90fce356_fk_products_" IMMEDIATE;
--
-- Add field product_id to products_combinations
--
ALTER TABLE "products_products_combinations" ADD COLUMN "product_id_id" bigint NOT NULL CONSTRAINT "products_products_co_product_id_id_230dcb6a_fk_products_" REFERENCES "products_products"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_products_co_product_id_id_230dcb6a_fk_products_" IMMEDIATE;
--
-- Add field brand_id to products
--
ALTER TABLE "products_products" ADD COLUMN "brand_id_id" bigint NULL CONSTRAINT "products_products_brand_id_id_b786179d_fk_products_brand_id" REFERENCES "products_brand"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_products_brand_id_id_b786179d_fk_products_brand_id" IMMEDIATE;
--
-- Add field category_id to products
--
ALTER TABLE "products_products" ADD COLUMN "category_id_id" bigint NOT NULL CONSTRAINT "products_products_category_id_id_686ec3b5_fk_products_" REFERENCES "products_categories"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_products_category_id_id_686ec3b5_fk_products_" IMMEDIATE;
--
-- Add field subcategory_id to products
--
ALTER TABLE "products_products" ADD COLUMN "subcategory_id_id" bigint NOT NULL CONSTRAINT "products_products_subcategory_id_id_22f90e74_fk_products_" REFERENCES "products_subcategories"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_products_subcategory_id_id_22f90e74_fk_products_" IMMEDIATE;
--
-- Add field product_variation_id to product_variations_options
--
ALTER TABLE "products_product_variations_options" ADD COLUMN "product_variation_id_id" bigint NOT NULL CONSTRAINT "products_product_var_product_variation_id_135c5e53_fk_products_" REFERENCES "products_product_variations"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_product_var_product_variation_id_135c5e53_fk_products_" IMMEDIATE;
--
-- Add field product_id to product_variations
--
ALTER TABLE "products_product_variations" ADD COLUMN "product_id_id" bigint NOT NULL CONSTRAINT "products_product_var_product_id_id_a96b61f2_fk_products_" REFERENCES "products_products"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_product_var_product_id_id_a96b61f2_fk_products_" IMMEDIATE;
--
-- Add field image_galleries_id to product_images
--
ALTER TABLE "products_product_images" ADD COLUMN "image_galleries_id_id" bigint NOT NULL CONSTRAINT "products_product_ima_image_galleries_id_i_17ff07c6_fk_products_" REFERENCES "products_image_galleries"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_product_ima_image_galleries_id_i_17ff07c6_fk_products_" IMMEDIATE;
--
-- Add field product_variations_value_id to product_images
--
ALTER TABLE "products_product_images" ADD COLUMN "product_variations_value_id_id" bigint NOT NULL CONSTRAINT "products_product_ima_product_variations_v_7d7f68aa_fk_products_" REFERENCES "products_products_combinations"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_product_ima_product_variations_v_7d7f68aa_fk_products_" IMMEDIATE;
--
-- Add field product_id to product_cache
--
ALTER TABLE "products_product_cache" ADD COLUMN "product_id_id" bigint NOT NULL CONSTRAINT "products_product_cac_product_id_id_fde43cf9_fk_products_" REFERENCES "products_products"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_product_cac_product_id_id_fde43cf9_fk_products_" IMMEDIATE;
--
-- Add field festive_season to festiveseasonproducts
--
ALTER TABLE "products_festiveseasonproducts" ADD COLUMN "festive_season_id" bigint NOT NULL CONSTRAINT "products_festiveseas_festive_season_id_0b989549_fk_products_" REFERENCES "products_festiveseasons"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_festiveseas_festive_season_id_0b989549_fk_products_" IMMEDIATE;
--
-- Add field products to festiveseasonproducts
--
ALTER TABLE "products_festiveseasonproducts" ADD COLUMN "products_id" bigint NOT NULL CONSTRAINT "products_festiveseas_products_id_587d924f_fk_products_" REFERENCES "products_products"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_festiveseas_products_id_587d924f_fk_products_" IMMEDIATE;
--
-- Add field category to commoncategories
--
ALTER TABLE "products_commoncategories" ADD COLUMN "category_id" bigint NOT NULL CONSTRAINT "products_commoncateg_category_id_34e43ce9_fk_products_" REFERENCES "products_categories"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_commoncateg_category_id_34e43ce9_fk_products_" IMMEDIATE;
--
-- Add field client_session to clientsessionwishlistmap
--
ALTER TABLE "products_clientsessionwishlistmap" ADD COLUMN "client_session_id" uuid NOT NULL CONSTRAINT "products_clientsessi_client_session_id_a425de67_fk_products_" REFERENCES "products_clientsession"("uid") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_clientsessi_client_session_id_a425de67_fk_products_" IMMEDIATE;
--
-- Add field product_combinations to clientsessionwishlistmap
--
ALTER TABLE "products_clientsessionwishlistmap" ADD COLUMN "product_combinations_id" bigint NOT NULL CONSTRAINT "products_clientsessi_product_combinations_be9e48b6_fk_products_" REFERENCES "products_products_combinations"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_clientsessi_product_combinations_be9e48b6_fk_products_" IMMEDIATE;
--
-- Add field products to clientsessionwishlistmap
--
ALTER TABLE "products_clientsessionwishlistmap" ADD COLUMN "products_id" bigint NOT NULL CONSTRAINT "products_clientsessi_products_id_619c9197_fk_products_" REFERENCES "products_products"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_clientsessi_products_id_619c9197_fk_products_" IMMEDIATE;
--
-- Add field client_session to clientsessioncartmap
--
ALTER TABLE "products_clientsessioncartmap" ADD COLUMN "client_session_id" uuid NOT NULL CONSTRAINT "products_clientsessi_client_session_id_64c80beb_fk_products_" REFERENCES "products_clientsession"("uid") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_clientsessi_client_session_id_64c80beb_fk_products_" IMMEDIATE;
--
-- Add field products to clientsessioncartmap
--
ALTER TABLE "products_clientsessioncartmap" ADD COLUMN "products_id" bigint NOT NULL CONSTRAINT "products_clientsessi_products_id_88d393cd_fk_products_" REFERENCES "products_products_combinations"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_clientsessi_products_id_88d393cd_fk_products_" IMMEDIATE;
--
-- Add field logged_user to clientsession
--
ALTER TABLE "products_clientsession" ADD COLUMN "logged_user_id" bigint NULL CONSTRAINT "products_clientsession_logged_user_id_10ac3b90_fk_user_user_id" REFERENCES "user_user"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "products_clientsession_logged_user_id_10ac3b90_fk_user_user_id" IMMEDIATE;
--
-- Alter unique_together for subcategories (1 constraint(s))
--
ALTER TABLE "products_subcategories" ADD CONSTRAINT "products_subcategories_subcategoryName_category_f1966f80_uniq" UNIQUE ("subcategoryName", "category_id_id");
CREATE INDEX "products_reviewproducts_user_id_4e2de819" ON "products_reviewproducts" ("user_id");
CREATE INDEX "products_products_stocks_products_combinations_id_id_90fce356" ON "products_products_stocks" ("products_combinations_id_id");
CREATE INDEX "products_products_combinations_product_id_id_230dcb6a" ON "products_products_combinations" ("product_id_id");
CREATE INDEX "products_products_brand_id_id_b786179d" ON "products_products" ("brand_id_id");
CREATE INDEX "products_products_category_id_id_686ec3b5" ON "products_products" ("category_id_id");
CREATE INDEX "products_products_subcategory_id_id_22f90e74" ON "products_products" ("subcategory_id_id");
CREATE INDEX "products_product_variation_product_variation_id_id_135c5e53" ON "products_product_variations_options" ("product_variation_id_id");
CREATE INDEX "products_product_variations_product_id_id_a96b61f2" ON "products_product_variations" ("product_id_id");
CREATE INDEX "products_product_images_image_galleries_id_id_17ff07c6" ON "products_product_images" ("image_galleries_id_id");
CREATE INDEX "products_product_images_product_variations_value_id_id_7d7f68aa" ON "products_product_images" ("product_variations_value_id_id");
CREATE INDEX "products_product_cache_product_id_id_fde43cf9" ON "products_product_cache" ("product_id_id");
CREATE INDEX "products_festiveseasonproducts_festive_season_id_0b989549" ON "products_festiveseasonproducts" ("festive_season_id");
CREATE INDEX "products_festiveseasonproducts_products_id_587d924f" ON "products_festiveseasonproducts" ("products_id");
CREATE INDEX "products_commoncategories_category_id_34e43ce9" ON "products_commoncategories" ("category_id");
CREATE INDEX "products_clientsessionwishlistmap_client_session_id_a425de67" ON "products_clientsessionwishlistmap" ("client_session_id");
CREATE INDEX "products_clientsessionwish_product_combinations_id_be9e48b6" ON "products_clientsessionwishlistmap" ("product_combinations_id");
CREATE INDEX "products_clientsessionwishlistmap_products_id_619c9197" ON "products_clientsessionwishlistmap" ("products_id");
CREATE INDEX "products_clientsessioncartmap_client_session_id_64c80beb" ON "products_clientsessioncartmap" ("client_session_id");
CREATE INDEX "products_clientsessioncartmap_products_id_88d393cd" ON "products_clientsessioncartmap" ("products_id");
CREATE INDEX "products_clientsession_logged_user_id_10ac3b90" ON "products_clientsession" ("logged_user_id");
COMMIT;
