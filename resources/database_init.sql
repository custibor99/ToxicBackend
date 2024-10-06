CREATE EXTENSION vector;

CREATE TABLE "chemical" (
  "id" integer PRIMARY KEY,
  "standardized_smile" varchar,
  "created_at" timestamp,
  "morgan_fingerprint" vector,
  "statistical_features" vector
);

CREATE TABLE "model" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "typeId" integer,
  "created_at" timestamp
);

CREATE TABLE "modelType" (
  "id" integer PRIMARY KEY,
  "type" varchar
);

CREATE TABLE "endpoint" (
  "id" integer PRIMARY KEY,
  "type" varchar
);

CREATE TABLE "prediction" (
  "id" integer PRIMARY KEY,
  "chemicalId" integer,
  "modelId" integer,
  "endpointId" integer,
  "created_at" timestamp
);

ALTER TABLE "model" ADD FOREIGN KEY ("typeId") REFERENCES "modelType" ("id");

ALTER TABLE "prediction" ADD FOREIGN KEY ("modelId") REFERENCES "model" ("id");

ALTER TABLE "prediction" ADD FOREIGN KEY ("chemicalId") REFERENCES "chemical" ("id");

ALTER TABLE "prediction" ADD FOREIGN KEY ("endpointId") REFERENCES "endpoint" ("id");
