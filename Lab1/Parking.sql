--
-- PostgreSQL database dump
--

-- Dumped from database version 12.8 (Ubuntu 12.8-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 14.0

-- Started on 2021-10-20 19:13:52

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 203 (class 1259 OID 16752)
-- Name: CarType; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."CarType" (
    "CarTypeID" smallint NOT NULL,
    "CarTypeName" character varying NOT NULL
);


ALTER TABLE public."CarType" OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16750)
-- Name: CarType_CarTypeID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."CarType" ALTER COLUMN "CarTypeID" ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public."CarType_CarTypeID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 206 (class 1259 OID 16770)
-- Name: Cars; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Cars" (
    "CarRegNum" character varying(8) NOT NULL,
    "CarMakeID" smallint NOT NULL,
    "CarType" smallint
);


ALTER TABLE public."Cars" OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16802)
-- Name: Contract; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Contract" (
    "ContractID" smallint NOT NULL,
    "CarNumber" character varying(8) NOT NULL,
    "PersonID" bigint NOT NULL,
    "ParkingID" smallint NOT NULL,
    "ContractStart" date NOT NULL,
    "ContractEnd" date NOT NULL
);


ALTER TABLE public."Contract" OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16800)
-- Name: Contract_ContractID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Contract" ALTER COLUMN "ContractID" ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public."Contract_ContractID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 205 (class 1259 OID 16762)
-- Name: Makes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Makes" (
    "MakeID" smallint NOT NULL,
    "MakeName" character varying(50) NOT NULL,
    "MakeDescription" text
);


ALTER TABLE public."Makes" OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16760)
-- Name: Makes_MakeID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Makes" ALTER COLUMN "MakeID" ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public."Makes_MakeID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 208 (class 1259 OID 16787)
-- Name: ParkingPlace; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."ParkingPlace" (
    "ParkingPlaceID" smallint NOT NULL,
    "ParkingPlaceDesc" text
);


ALTER TABLE public."ParkingPlace" OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 16785)
-- Name: ParkingPlace_ParkingPlaceID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."ParkingPlace" ALTER COLUMN "ParkingPlaceID" ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public."ParkingPlace_ParkingPlaceID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 50
    CACHE 1
);


--
-- TOC entry 209 (class 1259 OID 16795)
-- Name: Persons; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Persons" (
    "PersonID" bigint NOT NULL,
    "PersonLastName" character varying(50) NOT NULL,
    "PersonName" character varying(50) NOT NULL,
    "PersonMidleName" character varying(50)
);


ALTER TABLE public."Persons" OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16822)
-- Name: Phones; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Phones" (
    "Pnone" bigint NOT NULL,
    "PersonID" bigint NOT NULL
);


ALTER TABLE public."Phones" OWNER TO postgres;

--
-- TOC entry 2830 (class 2606 OID 16759)
-- Name: CarType CarType_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."CarType"
    ADD CONSTRAINT "CarType_pkey" PRIMARY KEY ("CarTypeID");


--
-- TOC entry 2834 (class 2606 OID 16774)
-- Name: Cars Cars_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cars"
    ADD CONSTRAINT "Cars_pkey" PRIMARY KEY ("CarRegNum");


--
-- TOC entry 2840 (class 2606 OID 16806)
-- Name: Contract Contract_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Contract"
    ADD CONSTRAINT "Contract_pkey" PRIMARY KEY ("ContractID");


--
-- TOC entry 2832 (class 2606 OID 16769)
-- Name: Makes Makes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Makes"
    ADD CONSTRAINT "Makes_pkey" PRIMARY KEY ("MakeID");


--
-- TOC entry 2836 (class 2606 OID 16794)
-- Name: ParkingPlace ParkingPlace_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."ParkingPlace"
    ADD CONSTRAINT "ParkingPlace_pkey" PRIMARY KEY ("ParkingPlaceID");


--
-- TOC entry 2838 (class 2606 OID 16865)
-- Name: Persons Persons_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Persons"
    ADD CONSTRAINT "Persons_pkey" PRIMARY KEY ("PersonID");


--
-- TOC entry 2842 (class 2606 OID 16826)
-- Name: Phones Phones_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Phones"
    ADD CONSTRAINT "Phones_pkey" PRIMARY KEY ("Pnone");


--
-- TOC entry 2843 (class 2606 OID 16775)
-- Name: Cars Cars_CarMakeID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cars"
    ADD CONSTRAINT "Cars_CarMakeID_fkey" FOREIGN KEY ("CarMakeID") REFERENCES public."Makes"("MakeID") ON UPDATE CASCADE;


--
-- TOC entry 2844 (class 2606 OID 16780)
-- Name: Cars Cars_CarType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cars"
    ADD CONSTRAINT "Cars_CarType_fkey" FOREIGN KEY ("CarType") REFERENCES public."CarType"("CarTypeID") ON UPDATE CASCADE;


--
-- TOC entry 2845 (class 2606 OID 16807)
-- Name: Contract Contract_CarNumber_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Contract"
    ADD CONSTRAINT "Contract_CarNumber_fkey" FOREIGN KEY ("CarNumber") REFERENCES public."Cars"("CarRegNum") ON UPDATE CASCADE;


--
-- TOC entry 2846 (class 2606 OID 16812)
-- Name: Contract Contract_ParkingID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Contract"
    ADD CONSTRAINT "Contract_ParkingID_fkey" FOREIGN KEY ("ParkingID") REFERENCES public."ParkingPlace"("ParkingPlaceID") ON UPDATE CASCADE;


--
-- TOC entry 2847 (class 2606 OID 16889)
-- Name: Contract Contract_PersonID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Contract"
    ADD CONSTRAINT "Contract_PersonID_fkey" FOREIGN KEY ("PersonID") REFERENCES public."Persons"("PersonID") ON UPDATE CASCADE;


--
-- TOC entry 2848 (class 2606 OID 16880)
-- Name: Phones Phones_PersonID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Phones"
    ADD CONSTRAINT "Phones_PersonID_fkey" FOREIGN KEY ("PersonID") REFERENCES public."Persons"("PersonID") ON UPDATE CASCADE;


-- Completed on 2021-10-20 19:13:53

--
-- PostgreSQL database dump complete
--

