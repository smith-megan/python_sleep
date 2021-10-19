create table age (
  "age" INT not null,
  "avg_age_hours" INT not null
);

create table tips (
  "id" int not null,
  "tip" VARCHAR(250),
  "source" VARCHAR(100),
  "link" VARCHAR(100)
);

create table user_tips (
  user_id INT NOT NULL REFERENCES user(user_id),
  tip_id INT NOT NULL REFERENCES tips(tip_id)
);

create table times (
  "user_id" INT NOT NULL REFERENCES user(user_id),
  "date_id" INT,
  "date" date,
  "morning" date,
  "night" date,
  "week_id" INT
  -- "hours" morning-night AS difference
);

create table "notes" (
"user_id" INT NOT NULL REFERENCES user(user_id),
"week_id" INT NOT NULL REFERENCES times(week_id),
"note" VARCHAR(200)
);

create table user(
  "id" int,
  "username" VARCHAR(40),
  "password" VARCHAR(40),
  "email" VARCHAR(40),
  "zipcode" INT not null,
  "birthday" date
);