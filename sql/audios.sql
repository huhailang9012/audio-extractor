/*
 Navicat Premium Data Transfer

 Source Server         : ar
 Source Server Type    : PostgreSQL
 Source Server Version : 100014
 Source Host           : localhost:5432
 Source Catalog        : audio_extracting
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 100014
 File Encoding         : 65001

 Date: 23/11/2020 16:01:06
*/


-- ----------------------------
-- Table structure for audios
-- ----------------------------
DROP TABLE IF EXISTS "public"."audios";
CREATE TABLE "public"."audios" (
  "id" char(32) COLLATE "pg_catalog"."default" NOT NULL,
  "name" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "md5" char(32) COLLATE "pg_catalog"."default" NOT NULL,
  "video_id" char(32) COLLATE "pg_catalog"."default" NOT NULL,
  "local_audio_path" varchar(512) COLLATE "pg_catalog"."default" NOT NULL,
  "date_created" char(19) COLLATE "pg_catalog"."default" NOT NULL,
  "format" varchar(8) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Primary Key structure for table audios
-- ----------------------------
ALTER TABLE "public"."audios" ADD CONSTRAINT "audios_pkey" PRIMARY KEY ("id");
