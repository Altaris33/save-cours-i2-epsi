create 'film', 'film_id', 'title', 'description', 'release_year', 'lang_id', 'rental_duration', 'rental_rate', 'length', 'rating'
create 'inventory', 'inventory_id', 'film_id', 'rental_id', 'store_id'  

create 'customer', 'customer_id', 'first_name', 'last_name', 'email', 'active'
create 'customer_address', 'address_id', 'address1', 'address2', 'district', 'city' 
create 'store', 'store_id', 'managaer_staff_id', 'address'
create 'store_address', 'store_address_id', 'address'