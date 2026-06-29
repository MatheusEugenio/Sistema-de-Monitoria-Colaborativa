--
-- PostgreSQL database dump
--

\restrict kpAwzlz6bRGFYLAyMydvwYb3LSo7gAOdkdtYWZwxtZWsaSzCEmUnXzAu5VpMq5f

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

-- Started on 2026-06-28 21:45:22 -03

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 885 (class 1247 OID 17591)
-- Name: chamada; Type: TYPE; Schema: public; Owner: -
--

CREATE TYPE public.chamada AS ENUM (
    'P',
    'F'
);


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 220 (class 1259 OID 17596)
-- Name: aluno; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.aluno (
    id_aluno integer NOT NULL,
    matricula integer NOT NULL,
    cpf character varying(15) NOT NULL,
    nome_curso character varying(50) NOT NULL,
    id_usuario integer NOT NULL
);


--
-- TOC entry 219 (class 1259 OID 17595)
-- Name: aluno_id_aluno_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.aluno_id_aluno_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4652 (class 0 OID 0)
-- Dependencies: 219
-- Name: aluno_id_aluno_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.aluno_id_aluno_seq OWNED BY public.aluno.id_aluno;


--
-- TOC entry 222 (class 1259 OID 17612)
-- Name: avisos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.avisos (
    id_aviso integer NOT NULL,
    titulo character varying(30) NOT NULL,
    conteudo text NOT NULL,
    data_publicacao date NOT NULL,
    usuario_id integer NOT NULL
);


--
-- TOC entry 221 (class 1259 OID 17611)
-- Name: avisos_id_aviso_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.avisos_id_aviso_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4653 (class 0 OID 0)
-- Dependencies: 221
-- Name: avisos_id_aviso_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.avisos_id_aviso_seq OWNED BY public.avisos.id_aviso;


--
-- TOC entry 224 (class 1259 OID 17626)
-- Name: certificado; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.certificado (
    id_certificado integer NOT NULL,
    semestre_letivo character varying(15) NOT NULL,
    data_emissao date NOT NULL,
    codigo_autentificacao character varying(30) NOT NULL,
    total_horas integer NOT NULL,
    id_monitor integer NOT NULL
);


--
-- TOC entry 223 (class 1259 OID 17625)
-- Name: certificado_id_certificado_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.certificado_id_certificado_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4654 (class 0 OID 0)
-- Dependencies: 223
-- Name: certificado_id_certificado_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.certificado_id_certificado_seq OWNED BY public.certificado.id_certificado;


--
-- TOC entry 226 (class 1259 OID 17641)
-- Name: disciplina; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.disciplina (
    id_disciplina integer NOT NULL,
    nome character varying(30) NOT NULL,
    carga_horaria integer NOT NULL,
    semestre character varying(10) NOT NULL
);


--
-- TOC entry 225 (class 1259 OID 17640)
-- Name: disciplina_id_disciplina_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.disciplina_id_disciplina_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4655 (class 0 OID 0)
-- Dependencies: 225
-- Name: disciplina_id_disciplina_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.disciplina_id_disciplina_seq OWNED BY public.disciplina.id_disciplina;


--
-- TOC entry 228 (class 1259 OID 17654)
-- Name: disponibilidade; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.disponibilidade (
    id_disponibilidade integer NOT NULL,
    horario_inicio time without time zone NOT NULL,
    horario_final time without time zone NOT NULL,
    data_inicio date NOT NULL,
    data_fim date NOT NULL,
    dia_semana character varying(15) NOT NULL,
    id_monitor integer NOT NULL
);


--
-- TOC entry 227 (class 1259 OID 17653)
-- Name: disponibilidade_id_disponibilidade_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.disponibilidade_id_disponibilidade_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4656 (class 0 OID 0)
-- Dependencies: 227
-- Name: disponibilidade_id_disponibilidade_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.disponibilidade_id_disponibilidade_seq OWNED BY public.disponibilidade.id_disponibilidade;


--
-- TOC entry 230 (class 1259 OID 17668)
-- Name: fila_espera; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.fila_espera (
    data_entrada date NOT NULL,
    posicao integer NOT NULL,
    id_aluno integer NOT NULL,
    id_sessao integer NOT NULL
);


--
-- TOC entry 229 (class 1259 OID 17667)
-- Name: fila_espera_posicao_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.fila_espera_posicao_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4657 (class 0 OID 0)
-- Dependencies: 229
-- Name: fila_espera_posicao_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.fila_espera_posicao_seq OWNED BY public.fila_espera.posicao;


--
-- TOC entry 232 (class 1259 OID 17679)
-- Name: frequencia; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.frequencia (
    id_frequencia integer NOT NULL,
    presente public.chamada NOT NULL,
    hora_entrada time without time zone NOT NULL,
    hora_saida time without time zone NOT NULL,
    id_aluno integer NOT NULL,
    id_sessao integer NOT NULL
);


--
-- TOC entry 231 (class 1259 OID 17678)
-- Name: frequencia_id_frequencia_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.frequencia_id_frequencia_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4658 (class 0 OID 0)
-- Dependencies: 231
-- Name: frequencia_id_frequencia_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.frequencia_id_frequencia_seq OWNED BY public.frequencia.id_frequencia;


--
-- TOC entry 234 (class 1259 OID 17694)
-- Name: material; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.material (
    id_material integer NOT NULL,
    descricao text NOT NULL,
    titulo character varying(15) NOT NULL,
    tipo_arquivo character varying(10) NOT NULL,
    link_arquivo character varying(30) NOT NULL,
    usuario_id integer NOT NULL
);


--
-- TOC entry 233 (class 1259 OID 17693)
-- Name: material_id_material_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.material_id_material_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4659 (class 0 OID 0)
-- Dependencies: 233
-- Name: material_id_material_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.material_id_material_seq OWNED BY public.material.id_material;


--
-- TOC entry 235 (class 1259 OID 17708)
-- Name: matricula_se; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.matricula_se (
    id_aluno integer NOT NULL,
    id_disciplina integer NOT NULL,
    id_turma integer NOT NULL
);


--
-- TOC entry 236 (class 1259 OID 17716)
-- Name: ministra; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ministra (
    professor_id integer NOT NULL,
    disciplina_id integer NOT NULL
);


--
-- TOC entry 238 (class 1259 OID 17724)
-- Name: monitor; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.monitor (
    id_monitor integer NOT NULL,
    departamento character varying(50) NOT NULL,
    id_aluno integer NOT NULL
);


--
-- TOC entry 237 (class 1259 OID 17723)
-- Name: monitor_id_monitor_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.monitor_id_monitor_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4660 (class 0 OID 0)
-- Dependencies: 237
-- Name: monitor_id_monitor_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.monitor_id_monitor_seq OWNED BY public.monitor.id_monitor;


--
-- TOC entry 240 (class 1259 OID 17734)
-- Name: monitoria; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.monitoria (
    id_monitoria integer NOT NULL,
    id_monitor integer NOT NULL,
    id_disciplina integer NOT NULL
);


--
-- TOC entry 239 (class 1259 OID 17733)
-- Name: monitoria_id_monitoria_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.monitoria_id_monitoria_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4661 (class 0 OID 0)
-- Dependencies: 239
-- Name: monitoria_id_monitoria_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.monitoria_id_monitoria_seq OWNED BY public.monitoria.id_monitoria;


--
-- TOC entry 242 (class 1259 OID 17744)
-- Name: professor; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.professor (
    id_professor integer NOT NULL,
    departamento character varying(50) NOT NULL,
    usuario_id integer NOT NULL
);


--
-- TOC entry 241 (class 1259 OID 17743)
-- Name: professor_id_professor_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.professor_id_professor_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4662 (class 0 OID 0)
-- Dependencies: 241
-- Name: professor_id_professor_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.professor_id_professor_seq OWNED BY public.professor.id_professor;


--
-- TOC entry 244 (class 1259 OID 17754)
-- Name: reserva; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reserva (
    id_reserva integer NOT NULL,
    data_reserva date NOT NULL,
    status character varying(30) NOT NULL,
    id_aluno integer NOT NULL,
    id_sessao integer NOT NULL
);


--
-- TOC entry 243 (class 1259 OID 17753)
-- Name: reserva_id_reserva_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reserva_id_reserva_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4663 (class 0 OID 0)
-- Dependencies: 243
-- Name: reserva_id_reserva_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reserva_id_reserva_seq OWNED BY public.reserva.id_reserva;


--
-- TOC entry 246 (class 1259 OID 17768)
-- Name: sessao; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.sessao (
    id_sessao integer NOT NULL,
    limite_participantes integer NOT NULL,
    horario time without time zone NOT NULL,
    descricao text NOT NULL,
    data date NOT NULL,
    id_monitoria integer NOT NULL
);


--
-- TOC entry 245 (class 1259 OID 17767)
-- Name: sessao_id_sessao_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.sessao_id_sessao_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4664 (class 0 OID 0)
-- Dependencies: 245
-- Name: sessao_id_sessao_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.sessao_id_sessao_seq OWNED BY public.sessao.id_sessao;


--
-- TOC entry 248 (class 1259 OID 17783)
-- Name: turma; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.turma (
    id_turma integer NOT NULL,
    semestre character varying(30) NOT NULL,
    codigo character varying(15) NOT NULL,
    disciplina_id integer NOT NULL,
    horario time without time zone NOT NULL
);


--
-- TOC entry 247 (class 1259 OID 17782)
-- Name: turma_id_turma_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.turma_id_turma_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4665 (class 0 OID 0)
-- Dependencies: 247
-- Name: turma_id_turma_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.turma_id_turma_seq OWNED BY public.turma.id_turma;


--
-- TOC entry 250 (class 1259 OID 17795)
-- Name: usuario; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.usuario (
    id_user integer NOT NULL,
    nome character varying(30) NOT NULL,
    email character varying(50) NOT NULL
);


--
-- TOC entry 249 (class 1259 OID 17794)
-- Name: usuario_id_user_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.usuario_id_user_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4666 (class 0 OID 0)
-- Dependencies: 249
-- Name: usuario_id_user_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.usuario_id_user_seq OWNED BY public.usuario.id_user;


--
-- TOC entry 252 (class 1259 OID 17805)
-- Name: validacao; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.validacao (
    id_validacao integer NOT NULL,
    data_validacao date NOT NULL,
    total_horas integer NOT NULL,
    status_validacao character varying(20) NOT NULL,
    id_professor integer NOT NULL,
    id_monitor integer NOT NULL
);


--
-- TOC entry 251 (class 1259 OID 17804)
-- Name: validacao_id_validacao_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.validacao_id_validacao_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4667 (class 0 OID 0)
-- Dependencies: 251
-- Name: validacao_id_validacao_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.validacao_id_validacao_seq OWNED BY public.validacao.id_validacao;


--
-- TOC entry 4412 (class 2604 OID 17599)
-- Name: aluno id_aluno; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.aluno ALTER COLUMN id_aluno SET DEFAULT nextval('public.aluno_id_aluno_seq'::regclass);


--
-- TOC entry 4413 (class 2604 OID 17615)
-- Name: avisos id_aviso; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.avisos ALTER COLUMN id_aviso SET DEFAULT nextval('public.avisos_id_aviso_seq'::regclass);


--
-- TOC entry 4414 (class 2604 OID 17629)
-- Name: certificado id_certificado; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.certificado ALTER COLUMN id_certificado SET DEFAULT nextval('public.certificado_id_certificado_seq'::regclass);


--
-- TOC entry 4415 (class 2604 OID 17644)
-- Name: disciplina id_disciplina; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.disciplina ALTER COLUMN id_disciplina SET DEFAULT nextval('public.disciplina_id_disciplina_seq'::regclass);


--
-- TOC entry 4416 (class 2604 OID 17657)
-- Name: disponibilidade id_disponibilidade; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.disponibilidade ALTER COLUMN id_disponibilidade SET DEFAULT nextval('public.disponibilidade_id_disponibilidade_seq'::regclass);


--
-- TOC entry 4417 (class 2604 OID 17671)
-- Name: fila_espera posicao; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.fila_espera ALTER COLUMN posicao SET DEFAULT nextval('public.fila_espera_posicao_seq'::regclass);


--
-- TOC entry 4418 (class 2604 OID 17682)
-- Name: frequencia id_frequencia; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.frequencia ALTER COLUMN id_frequencia SET DEFAULT nextval('public.frequencia_id_frequencia_seq'::regclass);


--
-- TOC entry 4419 (class 2604 OID 17697)
-- Name: material id_material; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.material ALTER COLUMN id_material SET DEFAULT nextval('public.material_id_material_seq'::regclass);


--
-- TOC entry 4420 (class 2604 OID 17727)
-- Name: monitor id_monitor; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.monitor ALTER COLUMN id_monitor SET DEFAULT nextval('public.monitor_id_monitor_seq'::regclass);


--
-- TOC entry 4421 (class 2604 OID 17737)
-- Name: monitoria id_monitoria; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.monitoria ALTER COLUMN id_monitoria SET DEFAULT nextval('public.monitoria_id_monitoria_seq'::regclass);


--
-- TOC entry 4422 (class 2604 OID 17747)
-- Name: professor id_professor; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.professor ALTER COLUMN id_professor SET DEFAULT nextval('public.professor_id_professor_seq'::regclass);


--
-- TOC entry 4423 (class 2604 OID 17757)
-- Name: reserva id_reserva; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reserva ALTER COLUMN id_reserva SET DEFAULT nextval('public.reserva_id_reserva_seq'::regclass);


--
-- TOC entry 4424 (class 2604 OID 17771)
-- Name: sessao id_sessao; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sessao ALTER COLUMN id_sessao SET DEFAULT nextval('public.sessao_id_sessao_seq'::regclass);


--
-- TOC entry 4425 (class 2604 OID 17786)
-- Name: turma id_turma; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.turma ALTER COLUMN id_turma SET DEFAULT nextval('public.turma_id_turma_seq'::regclass);


--
-- TOC entry 4426 (class 2604 OID 17798)
-- Name: usuario id_user; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuario ALTER COLUMN id_user SET DEFAULT nextval('public.usuario_id_user_seq'::regclass);


--
-- TOC entry 4427 (class 2604 OID 17808)
-- Name: validacao id_validacao; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.validacao ALTER COLUMN id_validacao SET DEFAULT nextval('public.validacao_id_validacao_seq'::regclass);


--
-- TOC entry 4429 (class 2606 OID 17608)
-- Name: aluno aluno_cpf_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.aluno
    ADD CONSTRAINT aluno_cpf_key UNIQUE (cpf);


--
-- TOC entry 4431 (class 2606 OID 17610)
-- Name: aluno aluno_matricula_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.aluno
    ADD CONSTRAINT aluno_matricula_key UNIQUE (matricula);


--
-- TOC entry 4433 (class 2606 OID 17606)
-- Name: aluno aluno_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.aluno
    ADD CONSTRAINT aluno_pkey PRIMARY KEY (id_aluno);


--
-- TOC entry 4435 (class 2606 OID 17624)
-- Name: avisos avisos_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.avisos
    ADD CONSTRAINT avisos_pkey PRIMARY KEY (id_aviso);


--
-- TOC entry 4437 (class 2606 OID 17639)
-- Name: certificado certificado_codigo_autentificacao_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.certificado
    ADD CONSTRAINT certificado_codigo_autentificacao_key UNIQUE (codigo_autentificacao);


--
-- TOC entry 4439 (class 2606 OID 17637)
-- Name: certificado certificado_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.certificado
    ADD CONSTRAINT certificado_pkey PRIMARY KEY (id_certificado);


--
-- TOC entry 4441 (class 2606 OID 17652)
-- Name: disciplina disciplina_nome_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.disciplina
    ADD CONSTRAINT disciplina_nome_key UNIQUE (nome);


--
-- TOC entry 4443 (class 2606 OID 17650)
-- Name: disciplina disciplina_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.disciplina
    ADD CONSTRAINT disciplina_pkey PRIMARY KEY (id_disciplina);


--
-- TOC entry 4445 (class 2606 OID 17666)
-- Name: disponibilidade disponibilidade_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.disponibilidade
    ADD CONSTRAINT disponibilidade_pkey PRIMARY KEY (id_disponibilidade);


--
-- TOC entry 4447 (class 2606 OID 17677)
-- Name: fila_espera fila_espera_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.fila_espera
    ADD CONSTRAINT fila_espera_pkey PRIMARY KEY (id_aluno, id_sessao);


--
-- TOC entry 4449 (class 2606 OID 17692)
-- Name: frequencia frequencia_aluno_sessao_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.frequencia
    ADD CONSTRAINT frequencia_aluno_sessao_key UNIQUE (id_aluno, id_sessao);


--
-- TOC entry 4451 (class 2606 OID 17690)
-- Name: frequencia frequencia_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.frequencia
    ADD CONSTRAINT frequencia_pkey PRIMARY KEY (id_frequencia);


--
-- TOC entry 4453 (class 2606 OID 17707)
-- Name: material material_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.material
    ADD CONSTRAINT material_pkey PRIMARY KEY (id_material);


--
-- TOC entry 4455 (class 2606 OID 17715)
-- Name: matricula_se matricula_se_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.matricula_se
    ADD CONSTRAINT matricula_se_pkey PRIMARY KEY (id_aluno, id_disciplina, id_turma);


--
-- TOC entry 4457 (class 2606 OID 17722)
-- Name: ministra ministra_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ministra
    ADD CONSTRAINT ministra_pkey PRIMARY KEY (professor_id, disciplina_id);


--
-- TOC entry 4459 (class 2606 OID 17732)
-- Name: monitor monitor_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.monitor
    ADD CONSTRAINT monitor_pkey PRIMARY KEY (id_monitor);


--
-- TOC entry 4461 (class 2606 OID 17742)
-- Name: monitoria monitoria_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.monitoria
    ADD CONSTRAINT monitoria_pkey PRIMARY KEY (id_monitoria);


--
-- TOC entry 4463 (class 2606 OID 17752)
-- Name: professor professor_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.professor
    ADD CONSTRAINT professor_pkey PRIMARY KEY (id_professor);


--
-- TOC entry 4465 (class 2606 OID 17766)
-- Name: reserva reserva_aluno_sessao_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reserva
    ADD CONSTRAINT reserva_aluno_sessao_key UNIQUE (id_aluno, id_sessao);


--
-- TOC entry 4467 (class 2606 OID 17764)
-- Name: reserva reserva_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reserva
    ADD CONSTRAINT reserva_pkey PRIMARY KEY (id_reserva);


--
-- TOC entry 4469 (class 2606 OID 17781)
-- Name: sessao sessao_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sessao
    ADD CONSTRAINT sessao_pkey PRIMARY KEY (id_sessao);


--
-- TOC entry 4471 (class 2606 OID 17793)
-- Name: turma turma_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.turma
    ADD CONSTRAINT turma_pkey PRIMARY KEY (id_turma);


--
-- TOC entry 4473 (class 2606 OID 17803)
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id_user);


--
-- TOC entry 4475 (class 2606 OID 17816)
-- Name: validacao validacao_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.validacao
    ADD CONSTRAINT validacao_pkey PRIMARY KEY (id_validacao);


--
-- TOC entry 4480 (class 2606 OID 17837)
-- Name: fila_espera fk_aluno; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.fila_espera
    ADD CONSTRAINT fk_aluno FOREIGN KEY (id_aluno) REFERENCES public.aluno(id_aluno);


--
-- TOC entry 4482 (class 2606 OID 17847)
-- Name: frequencia fk_aluno; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.frequencia
    ADD CONSTRAINT fk_aluno FOREIGN KEY (id_aluno) REFERENCES public.aluno(id_aluno);


--
-- TOC entry 4485 (class 2606 OID 17862)
-- Name: matricula_se fk_aluno; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.matricula_se
    ADD CONSTRAINT fk_aluno FOREIGN KEY (id_aluno) REFERENCES public.aluno(id_aluno);


--
-- TOC entry 4490 (class 2606 OID 17887)
-- Name: monitor fk_aluno; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.monitor
    ADD CONSTRAINT fk_aluno FOREIGN KEY (id_aluno) REFERENCES public.aluno(id_aluno);


--
-- TOC entry 4494 (class 2606 OID 17907)
-- Name: reserva fk_aluno; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reserva
    ADD CONSTRAINT fk_aluno FOREIGN KEY (id_aluno) REFERENCES public.aluno(id_aluno);


--
-- TOC entry 4486 (class 2606 OID 17867)
-- Name: matricula_se fk_disciplina; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.matricula_se
    ADD CONSTRAINT fk_disciplina FOREIGN KEY (id_disciplina) REFERENCES public.disciplina(id_disciplina);


--
-- TOC entry 4488 (class 2606 OID 17882)
-- Name: ministra fk_disciplina; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ministra
    ADD CONSTRAINT fk_disciplina FOREIGN KEY (disciplina_id) REFERENCES public.disciplina(id_disciplina);


--
-- TOC entry 4491 (class 2606 OID 17892)
-- Name: monitoria fk_disciplina; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.monitoria
    ADD CONSTRAINT fk_disciplina FOREIGN KEY (id_disciplina) REFERENCES public.disciplina(id_disciplina);


--
-- TOC entry 4497 (class 2606 OID 17922)
-- Name: turma fk_disciplina; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.turma
    ADD CONSTRAINT fk_disciplina FOREIGN KEY (disciplina_id) REFERENCES public.disciplina(id_disciplina);


--
-- TOC entry 4478 (class 2606 OID 17827)
-- Name: certificado fk_monitor; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.certificado
    ADD CONSTRAINT fk_monitor FOREIGN KEY (id_monitor) REFERENCES public.monitor(id_monitor);


--
-- TOC entry 4479 (class 2606 OID 17832)
-- Name: disponibilidade fk_monitor; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.disponibilidade
    ADD CONSTRAINT fk_monitor FOREIGN KEY (id_monitor) REFERENCES public.monitor(id_monitor);


--
-- TOC entry 4492 (class 2606 OID 17897)
-- Name: monitoria fk_monitor; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.monitoria
    ADD CONSTRAINT fk_monitor FOREIGN KEY (id_monitor) REFERENCES public.monitor(id_monitor);


--
-- TOC entry 4498 (class 2606 OID 17927)
-- Name: validacao fk_monitor; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.validacao
    ADD CONSTRAINT fk_monitor FOREIGN KEY (id_monitor) REFERENCES public.monitor(id_monitor);


--
-- TOC entry 4496 (class 2606 OID 17917)
-- Name: sessao fk_monitoria; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sessao
    ADD CONSTRAINT fk_monitoria FOREIGN KEY (id_monitoria) REFERENCES public.monitoria(id_monitoria);


--
-- TOC entry 4489 (class 2606 OID 17877)
-- Name: ministra fk_professor; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ministra
    ADD CONSTRAINT fk_professor FOREIGN KEY (professor_id) REFERENCES public.professor(id_professor);


--
-- TOC entry 4499 (class 2606 OID 17932)
-- Name: validacao fk_professor; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.validacao
    ADD CONSTRAINT fk_professor FOREIGN KEY (id_professor) REFERENCES public.professor(id_professor);


--
-- TOC entry 4481 (class 2606 OID 17842)
-- Name: fila_espera fk_sessao; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.fila_espera
    ADD CONSTRAINT fk_sessao FOREIGN KEY (id_sessao) REFERENCES public.sessao(id_sessao);


--
-- TOC entry 4483 (class 2606 OID 17852)
-- Name: frequencia fk_sessao; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.frequencia
    ADD CONSTRAINT fk_sessao FOREIGN KEY (id_sessao) REFERENCES public.sessao(id_sessao);


--
-- TOC entry 4495 (class 2606 OID 17912)
-- Name: reserva fk_sessao; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reserva
    ADD CONSTRAINT fk_sessao FOREIGN KEY (id_sessao) REFERENCES public.sessao(id_sessao);


--
-- TOC entry 4487 (class 2606 OID 17872)
-- Name: matricula_se fk_turma; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.matricula_se
    ADD CONSTRAINT fk_turma FOREIGN KEY (id_turma) REFERENCES public.turma(id_turma);


--
-- TOC entry 4476 (class 2606 OID 17817)
-- Name: aluno fk_usuario; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.aluno
    ADD CONSTRAINT fk_usuario FOREIGN KEY (id_usuario) REFERENCES public.usuario(id_user);


--
-- TOC entry 4477 (class 2606 OID 17822)
-- Name: avisos fk_usuario; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.avisos
    ADD CONSTRAINT fk_usuario FOREIGN KEY (usuario_id) REFERENCES public.usuario(id_user);


--
-- TOC entry 4484 (class 2606 OID 17857)
-- Name: material fk_usuario; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.material
    ADD CONSTRAINT fk_usuario FOREIGN KEY (usuario_id) REFERENCES public.usuario(id_user);


--
-- TOC entry 4493 (class 2606 OID 17902)
-- Name: professor fk_usuario; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.professor
    ADD CONSTRAINT fk_usuario FOREIGN KEY (usuario_id) REFERENCES public.usuario(id_user);


-- Completed on 2026-06-28 21:45:22 -03

--
-- PostgreSQL database dump complete
--

\unrestrict kpAwzlz6bRGFYLAyMydvwYb3LSo7gAOdkdtYWZwxtZWsaSzCEmUnXzAu5VpMq5f

