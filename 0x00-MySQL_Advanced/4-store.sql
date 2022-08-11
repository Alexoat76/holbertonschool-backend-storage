-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
-- New & OLD are MySQL extensions to triggers
-- Enable to access columns in the rows affected by a trigger
-- Quantity in the table items can be negative.

CREATE TRIGGER decrease_quantity_item AFTER INSERT ON orders
    FOR EACH ROW
        UPDATE items SET quantity = quantity - NEW.number
        WHERE items.name = NEW.item_name;
