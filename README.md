# Inventory Management System(InvProject)

Simple Django inventory app to create, list, update and delete products.

## Contents
- App code: [Invapp](Invapp/)
- Main entry: [manage.py](manage.py)
- Settings: [InvProject/settings.py](InvProject/settings.py)
- Requirements: [requirements.txt](requirements.txt)

## Key files & symbols
- Model: [`Invapp.models.Product`](Invapp/models.py) — [Invapp/models.py](Invapp/models.py)  
- Forms: [`Invapp.forms.ProductForm`](Invapp/forms.py) — [Invapp/forms.py](Invapp/forms.py)  
- Views: [`Invapp.views.home_view`](Invapp/views.py), [`Invapp.views.product_create_view`](Invapp/views.py), [`Invapp.views.product_list_view`](Invapp/views.py), [`Invapp.views.product_update_view`](Invapp/views.py), [`Invapp.views.product_delete_view`](Invapp/views.py) — [Invapp/views.py](Invapp/views.py)  
- Templates: layout and pages — [Invapp/templates/Invapp/layout.html](Invapp/templates/Invapp/layout.html), [Invapp/templates/Invapp/product_list.html](Invapp/templates/Invapp/product_list.html), [Invapp/templates/Invapp/product_form.html](Invapp/templates/Invapp/product_form.html), [Invapp/templates/Invapp/product_confirm_delete.html](Invapp/templates/Invapp/product_confirm_delete.html)  
- Migrations: [Invapp/migrations/0001_initial.py](Invapp/migrations/0001_initial.py), [Invapp/migrations/0002_rename_category_product_supplier_and_more.py](Invapp/migrations/0002_rename_category_product_supplier_and_more.py)  
- Admin registration (currently empty): [Invapp/admin.py](Invapp/admin.py)

## Features
- Product model with: product_id, name, sku, price, quantity, supplier ([Invapp.models.Product](Invapp/models.py)).
- Create / Read / Update / Delete via views and templates ([Invapp/views.py](Invapp/views.py), [Invapp/forms.py](Invapp/forms.py)).
- Bootstrap-based UI in [Invapp/templates/Invapp/layout.html](Invapp/templates/Invapp/layout.html).

## Quick start (local)
1. Create and activate a virtual environment:
   - Windows:
     python -m venv venv
     venv\Scripts\activate
   - macOS/Linux:
     python3 -m venv venv
     source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Apply migrations:
   python manage.py migrate

   Note: This repo already contains migration files at [Invapp/migrations/](Invapp/migrations/). If you need a fresh DB, remove `db.sqlite3` then run migrations.

4. Run development server:
   python manage.py runserver

5. Open in browser:
   - Home: `/` (uses [`Invapp.views.home_view`](Invapp/views.py))
   - Add product: `/create/` (uses [`Invapp.views.product_create_view`](Invapp/views.py))
   - List products: `/list/` (uses [`Invapp.views.product_list_view`](Invapp/views.py))

## Development notes
- The model schema was changed via migrations: see [0001_initial.py](Invapp/migrations/0001_initial.py) and [0002_rename_category_product_supplier_and_more.py](Invapp/migrations/0002_rename_category_product_supplier_and_more.py).
- Admin site is not configured for the `Product` model. Register it in [Invapp/admin.py](Invapp/admin.py) if admin access is needed.
- Form widgets configured in [Invapp/forms.py](Invapp/forms.py) control form appearance.

## Useful links
- Django settings: [InvProject/settings.py](InvProject/settings.py)
- URL routing: [InvProject/urls.py](InvProject/urls.py), app urls: [Invapp/urls.py](Invapp/urls.py)
