create table age (
  "user_age" INT not null,
  "avg_age_hours" INT not null
);

create table tips (
  "tip_id" int not null,
  "tip" VARCHAR(250),
  "source" VARCHAR(100),
  "link" VARCHAR(100)
);

create table user_tips (
  user_id INT NOT NULL REFERENCES user(user_id),
  tip_id INT NOT NULL REFERENCES tips(tip_id)
);

create table times (
  "date_id" INT,
  "date" VARCHAR(40),
  "morning" VARCHAR(40),
  "night" VARCHAR(40),
  "week" INT
  -- "hours" morning-night
);

create table "notes" (
"user_id" INT NOT NULL REFERENCES user(user_id),
"week_id" INT NOT NULL REFERENCES times(week),
"note" VARCHAR(200)
);

create table user(
  "user_id" int,
  "username" VARCHAR(40),
  "password" VARCHAR(40),
  "email" VARCHAR(40),
  "zipcode" INT not null,
  "age" INT NOT NULL REFERENCES age(user_age)
  -- "hours"
  -- "times"
  -- "saved_tips"
);