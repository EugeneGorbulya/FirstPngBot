CREATE TABLE category (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    range_start BIGINT NOT NULL,
    range_end BIGINT NOT NULL
);

CREATE TABLE product (
    id BIGSERIAL PRIMARY KEY,
    category_id BIGINT REFERENCES category(id),
    rank_image_0 BIGINT DEFAULT 0,
    rank_image_1 BIGINT DEFAULT 0,
    rank_image_2 BIGINT DEFAULT 0,
    rank_image_3 BIGINT DEFAULT 0,
    rank_image_4 BIGINT DEFAULT 0
);

CREATE TABLE event (
    id BIGSERIAL PRIMARY KEY,
    chat_id BIGINT NOT NULL,
    product_id BIGINT REFERENCES product(id),
    image_index BIGINT NOT NULL
);
