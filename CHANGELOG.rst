1.0b1.dev1003
=============

 * added multilingual capabilities

Migrations
~~~~~~~~~~

Box model (added a nullable language field)::

    ALTER TABLE "boxes_box" ADD COLUMN "language" varchar(10);
    ALTER TABLE "boxes_box" ADD CONSTRAINT "boxes_box_lang_label" UNIQUE (language, label);

Templates
~~~~~~~~~

Two templates were added and are included in the app.  ``boxes/_links.html`` takes
single context variable ``links`` that is a list of tuples of (url, link text) that
is used for multilingual configurations. \

For single language use, the ``boxes/_link.html`` template is rendered with the
context variables ``link`` and ``link_text`` in order to render the create or
edit link. This was previously hard coded in the template tag but is now a template
so you can override in your project if need be.

The existing ``boxes/box_create.html`` and ``boxes/box_edit.html`` templates now
receive an additional context variable called ``lang`` which is the language code
for the content being edited. This is useful in multilingual configurations so as to
remind the user what language they are authoring.


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
