1.0b1
=====

 * added authorization checks on views
 * removed get_or_create in tag and only create now on initial submission of form.
 * added auditing

Migrations
~~~~~~~~~~

Box model (added created_by and last_updated_by columns as FK to User).::

    ALTER TABLE "boxes_box" ADD COLUMN "created_by_id" integer not null REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
    CREATE INDEX "boxes_box_created_by_id" ON "boxes_box" ("created_by_id");

Templates
~~~~~~~~~

A ``boxes/box_create.html`` was added that can be identical to
``boxes/box_edit.html`` just with a different action url.

URLs
~~~~

A new ``boxes_create`` url was added to support the rendering of the create
form as well as processing the POST of that form. It takes a ``[-\w]+`` parameter
which is the label.
