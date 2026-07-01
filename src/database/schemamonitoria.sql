--
-- PostgreSQL database dump
--

\restrict YuZpm4NdAcTY3DhJwEQ40yo27gx1mkQACyQy8iXk7mHIIlsxyRkVepUX6BlstV7

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

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
-- Name: chamada; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.chamada AS ENUM (
    'P',
    'F'
);


ALTER TYPE public.chamada OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: aluno; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aluno (
    id_aluno integer NOT NULL,
    matricula integer NOT NULL,
    cpf character varying(15) NOT NULL,
    nome_curso character varying(50) NOT NULL,
    id_usuario integer NOT NULL
);


ALTER TABLE public.aluno OWNER TO postgres;

--
-- Name: aluno_id_aluno_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.aluno_id_aluno_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.aluno_id_aluno_seq OWNER TO postgres;

--
-- Name: aluno_id_aluno_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.aluno_id_aluno_seq OWNED BY public.aluno.id_aluno;


--
-- Name: avisos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.avisos (
    id_aviso integer NOT NULL,
    titulo character varying(30) NOT NULL,
    conteudo text NOT NULL,
    data_publicacao date NOT NULL,
    usuario_id integer NOT NULL
);


ALTER TABLE public.avisos OWNER TO postgres;

--
-- Name: avisos_id_aviso_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.avisos_id_aviso_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.avisos_id_aviso_seq OWNER TO postgres;

--
-- Name: avisos_id_aviso_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.avisos_id_aviso_seq OWNED BY public.avisos.id_aviso;


--
-- Name: certificado; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.certificado (
    id_certificado integer NOT NULL,
    semestre_letivo character varying(15) NOT NULL,
    data_emissao date NOT NULL,
    codigo_autentificacao character varying(30) NOT NULL,
    total_horas integer NOT NULL,
    id_monitor integer NOT NULL
);


ALTER TABLE public.certificado OWNER TO postgres;

--
-- Name: certificado_id_certificado_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.certificado_id_certificado_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.certificado_id_certificado_seq OWNER TO postgres;

--
-- Name: certificado_id_certificado_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.certificado_id_certificado_seq OWNED BY public.certificado.id_certificado;


--
-- Name: disciplina; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.disciplina (
    id_disciplina integer NOT NULL,
    nome character varying(30) NOT NULL,
    carga_horaria integer NOT NULL,
    semestre character varying(10) NOT NULL
);


ALTER TABLE public.disciplina OWNER TO postgres;

--
-- Name: disciplina_id_disciplina_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.disciplina_id_disciplina_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.disciplina_id_disciplina_seq OWNER TO postgres;

--
-- Name: disciplina_id_disciplina_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.disciplina_id_disciplina_seq OWNED BY public.disciplina.id_disciplina;


--
-- Name: disponibilidade; Type: TABLE; Schema: public; Owner: postgres
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


ALTER TABLE public.disponibilidade OWNER TO postgres;

--
-- Name: disponibilidade_id_disponibilidade_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.disponibilidade_id_disponibilidade_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.disponibilidade_id_disponibilidade_seq OWNER TO postgres;

--
-- Name: disponibilidade_id_disponibilidade_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.disponibilidade_id_disponibilidade_seq OWNED BY public.disponibilidade.id_disponibilidade;


--
-- Name: fila_espera; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fila_espera (
    data_entrada date NOT NULL,
    posicao integer NOT NULL,
    id_aluno integer NOT NULL,
    id_sessao integer NOT NULL
);


ALTER TABLE public.fila_espera OWNER TO postgres;

--
-- Name: fila_espera_posicao_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fila_espera_posicao_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.fila_espera_posicao_seq OWNER TO postgres;

--
-- Name: fila_espera_posicao_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fila_espera_posicao_seq OWNED BY public.fila_espera.posicao;


--
-- Name: frequencia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.frequencia (
    id_frequencia integer NOT NULL,
    presente public.chamada NOT NULL,
    hora_entrada time without time zone NOT NULL,
    hora_saida time without time zone NOT NULL,
    id_aluno integer NOT NULL,
    id_sessao integer NOT NULL
);


ALTER TABLE public.frequencia OWNER TO postgres;

--
-- Name: frequencia_id_frequencia_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.frequencia_id_frequencia_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.frequencia_id_frequencia_seq OWNER TO postgres;

--
-- Name: frequencia_id_frequencia_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.frequencia_id_frequencia_seq OWNED BY public.frequencia.id_frequencia;


--
-- Name: material; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.material (
    id_material integer NOT NULL,
    descricao text NOT NULL,
    titulo character varying(15) NOT NULL,
    tipo_arquivo character varying(10) NOT NULL,
    link_arquivo character varying(30) NOT NULL,
    usuario_id integer NOT NULL
);


ALTER TABLE public.material OWNER TO postgres;

--
-- Name: material_id_material_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.material_id_material_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.material_id_material_seq OWNER TO postgres;

--
-- Name: material_id_material_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.material_id_material_seq OWNED BY public.material.id_material;


--
-- Name: matricula_se; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.matricula_se (
    id_aluno integer NOT NULL,
    id_disciplina integer NOT NULL,
    id_turma integer NOT NULL
);


ALTER TABLE public.matricula_se OWNER TO postgres;

--
-- Name: ministra; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ministra (
    professor_id integer NOT NULL,
    disciplina_id integer NOT NULL
);


ALTER TABLE public.ministra OWNER TO postgres;

--
-- Name: monitor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monitor (
    id_monitor integer NOT NULL,
    departamento character varying(50) NOT NULL,
    id_aluno integer NOT NULL
);


ALTER TABLE public.monitor OWNER TO postgres;

--
-- Name: monitor_id_monitor_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monitor_id_monitor_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.monitor_id_monitor_seq OWNER TO postgres;

--
-- Name: monitor_id_monitor_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monitor_id_monitor_seq OWNED BY public.monitor.id_monitor;


--
-- Name: monitoria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monitoria (
    id_monitoria integer NOT NULL,
    id_monitor integer NOT NULL,
    id_disciplina integer NOT NULL
);


ALTER TABLE public.monitoria OWNER TO postgres;

--
-- Name: monitoria_id_monitoria_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monitoria_id_monitoria_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.monitoria_id_monitoria_seq OWNER TO postgres;

--
-- Name: monitoria_id_monitoria_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monitoria_id_monitoria_seq OWNED BY public.monitoria.id_monitoria;


--
-- Name: professor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.professor (
    id_professor integer NOT NULL,
    departamento character varying(50) NOT NULL,
    usuario_id integer NOT NULL
);


ALTER TABLE public.professor OWNER TO postgres;

--
-- Name: professor_id_professor_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.professor_id_professor_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.professor_id_professor_seq OWNER TO postgres;

--
-- Name: professor_id_professor_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.professor_id_professor_seq OWNED BY public.professor.id_professor;


--
-- Name: reserva; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reserva (
    id_reserva integer NOT NULL,
    data_reserva date NOT NULL,
    status character varying(30) NOT NULL,
    id_aluno integer NOT NULL,
    id_sessao integer NOT NULL
);


ALTER TABLE public.reserva OWNER TO postgres;

--
-- Name: reserva_id_reserva_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reserva_id_reserva_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.reserva_id_reserva_seq OWNER TO postgres;

--
-- Name: reserva_id_reserva_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reserva_id_reserva_seq OWNED BY public.reserva.id_reserva;


--
-- Name: sessao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sessao (
    id_sessao integer NOT NULL,
    limite_participantes integer NOT NULL,
    horario time without time zone NOT NULL,
    descricao text NOT NULL,
    data date NOT NULL,
    id_monitoria integer NOT NULL
);


ALTER TABLE public.sessao OWNER TO postgres;

--
-- Name: sessao_id_sessao_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sessao_id_sessao_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sessao_id_sessao_seq OWNER TO postgres;

--
-- Name: sessao_id_sessao_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sessao_id_sessao_seq OWNED BY public.sessao.id_sessao;


--
-- Name: turma; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.turma (
    id_turma integer NOT NULL,
    semestre character varying(30) NOT NULL,
    codigo character varying(15) NOT NULL,
    disciplina_id integer NOT NULL,
    horario time without time zone NOT NULL
);


ALTER TABLE public.turma OWNER TO postgres;

--
-- Name: turma_id_turma_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.turma_id_turma_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.turma_id_turma_seq OWNER TO postgres;

--
-- Name: turma_id_turma_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.turma_id_turma_seq OWNED BY public.turma.id_turma;


--
-- Name: usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario (
    id_user integer NOT NULL,
    nome character varying(30) NOT NULL,
    email character varying(50) NOT NULL
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- Name: usuario_id_user_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuario_id_user_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.usuario_id_user_seq OWNER TO postgres;

--
-- Name: usuario_id_user_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuario_id_user_seq OWNED BY public.usuario.id_user;


--
-- Name: validacao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.validacao (
    id_validacao integer NOT NULL,
    data_validacao date NOT NULL,
    total_horas integer NOT NULL,
    status_validacao character varying(20) NOT NULL,
    id_professor integer NOT NULL,
    id_monitor integer NOT NULL
);


ALTER TABLE public.validacao OWNER TO postgres;

--
-- Name: validacao_id_validacao_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.validacao_id_validacao_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.validacao_id_validacao_seq OWNER TO postgres;

--
-- Name: validacao_id_validacao_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.validacao_id_validacao_seq OWNED BY public.validacao.id_validacao;


--
-- Name: aluno id_aluno; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aluno ALTER COLUMN id_aluno SET DEFAULT nextval('public.aluno_id_aluno_seq'::regclass);


--
-- Name: avisos id_aviso; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avisos ALTER COLUMN id_aviso SET DEFAULT nextval('public.avisos_id_aviso_seq'::regclass);


--
-- Name: certificado id_certificado; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.certificado ALTER COLUMN id_certificado SET DEFAULT nextval('public.certificado_id_certificado_seq'::regclass);


--
-- Name: disciplina id_disciplina; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.disciplina ALTER COLUMN id_disciplina SET DEFAULT nextval('public.disciplina_id_disciplina_seq'::regclass);


--
-- Name: disponibilidade id_disponibilidade; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.disponibilidade ALTER COLUMN id_disponibilidade SET DEFAULT nextval('public.disponibilidade_id_disponibilidade_seq'::regclass);


--
-- Name: fila_espera posicao; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fila_espera ALTER COLUMN posicao SET DEFAULT nextval('public.fila_espera_posicao_seq'::regclass);


--
-- Name: frequencia id_frequencia; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.frequencia ALTER COLUMN id_frequencia SET DEFAULT nextval('public.frequencia_id_frequencia_seq'::regclass);


--
-- Name: material id_material; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.material ALTER COLUMN id_material SET DEFAULT nextval('public.material_id_material_seq'::regclass);


--
-- Name: monitor id_monitor; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monitor ALTER COLUMN id_monitor SET DEFAULT nextval('public.monitor_id_monitor_seq'::regclass);


--
-- Name: monitoria id_monitoria; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monitoria ALTER COLUMN id_monitoria SET DEFAULT nextval('public.monitoria_id_monitoria_seq'::regclass);


--
-- Name: professor id_professor; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professor ALTER COLUMN id_professor SET DEFAULT nextval('public.professor_id_professor_seq'::regclass);


--
-- Name: reserva id_reserva; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reserva ALTER COLUMN id_reserva SET DEFAULT nextval('public.reserva_id_reserva_seq'::regclass);


--
-- Name: sessao id_sessao; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessao ALTER COLUMN id_sessao SET DEFAULT nextval('public.sessao_id_sessao_seq'::regclass);


--
-- Name: turma id_turma; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.turma ALTER COLUMN id_turma SET DEFAULT nextval('public.turma_id_turma_seq'::regclass);


--
-- Name: usuario id_user; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario ALTER COLUMN id_user SET DEFAULT nextval('public.usuario_id_user_seq'::regclass);


--
-- Name: validacao id_validacao; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.validacao ALTER COLUMN id_validacao SET DEFAULT nextval('public.validacao_id_validacao_seq'::regclass);


--
-- Data for Name: aluno; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.aluno (id_aluno, matricula, cpf, nome_curso, id_usuario) FROM stdin;
1	202601	111.111.111-11	Ciência da Computação	1
2	202602	222.222.222-22	Engenharia de Software	2
3	202603	333.333.333-33	Sistemas de Informação	3
4	202604	444.444.444-44	Ciência da Computação	4
5	202605	555.555.555-55	Engenharia de Software	5
6	202606	666.666.666-66	Sistemas de Informação	6
7	202607	777.777.777-77	Ciência da Computação	7
8	202608	888.888.888-88	Engenharia de Software	8
9	202609	999.999.999-99	Sistemas de Informação	9
10	202610	101.010.101-01	Ciência da Computação	10
11	202611	112.121.112-11	Engenharia de Software	11
12	202612	123.232.123-12	Sistemas de Informação	12
13	202613	134.343.134-13	Ciência da Computação	13
14	202614	145.454.145-14	Engenharia de Software	14
15	202615	156.565.156-15	Sistemas de Informação	15
\.


--
-- Data for Name: avisos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.avisos (id_aviso, titulo, conteudo, data_publicacao, usuario_id) FROM stdin;
1	Início das Monitorias	As monitorias começam nesta semana.	2026-03-01	1
2	Sala Alterada	A monitoria de Cálculo mudou para a sala 102.	2026-03-02	2
3	Material de Apoio	Novo material disponível na aba correspondente.	2026-03-03	3
4	Horário de Feriado	Não haverá monitoria no feriado municipal.	2026-03-04	4
5	Inscrições Abertas	Inscrições para novos monitores abertas.	2026-03-05	5
6	Instabilidade no Sistema	O sistema passará por manutenção preventiva.	2026-03-06	6
7	Oficina de Python	Participe da oficina básica de programação.	2026-03-07	7
8	Revisão para Prova	Sessão extra de revisão agendada.	2026-03-08	8
9	Certificados Prontos	Os certificados do semestre passado estão disponíveis.	2026-03-09	9
10	Aviso Importante	Atenção aos prazos de cancelamento de reservas.	2026-03-10	10
11	Dúvidas Frequentes	Confira o FAQ atualizado do programa.	2026-03-11	11
12	Pesquisa de Satisfação	Por favor, respondam o formulário enviado.	2026-03-12	12
13	Novo Monitor	Boas-vindas ao novo monitor de Redes.	2026-03-13	13
14	Encerramento	Último dia de monitorias do semestre.	2026-03-14	14
15	Planejamento 2026.2	Cronograma para o próximo semestre publicado.	2026-03-15	15
\.


--
-- Data for Name: certificado; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.certificado (id_certificado, semestre_letivo, data_emissao, codigo_autentificacao, total_horas, id_monitor) FROM stdin;
1	2026.1	2026-06-20	CERT-202601	60	1
2	2026.1	2026-06-20	CERT-202602	60	2
3	2026.1	2026-06-20	CERT-202603	60	3
4	2026.1	2026-06-20	CERT-202604	60	4
5	2026.1	2026-06-20	CERT-202605	60	5
6	2026.1	2026-06-20	CERT-202606	60	6
7	2026.1	2026-06-20	CERT-202607	60	7
8	2026.1	2026-06-20	CERT-202608	60	8
9	2026.1	2026-06-20	CERT-202609	60	9
10	2026.1	2026-06-20	CERT-202610	60	10
11	2026.1	2026-06-20	CERT-202611	60	11
12	2026.1	2026-06-20	CERT-202612	60	12
13	2026.1	2026-06-20	CERT-202613	60	13
14	2026.1	2026-06-20	CERT-202614	60	14
15	2026.1	2026-06-20	CERT-202615	60	15
\.


--
-- Data for Name: disciplina; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.disciplina (id_disciplina, nome, carga_horaria, semestre) FROM stdin;
1	Cálculo I	60	2026.1
2	Álgebra Linear	60	2026.1
3	Introdução à Programação	90	2026.1
4	Estrutura de Dados	60	2026.1
5	Banco de Dados I	60	2026.2
6	Engenharia de Software	60	2026.2
7	Sistemas Operacionais	60	2026.2
8	Redes de Computadores	60	2026.2
9	Física Mecânica	60	2026.1
10	Química Geral	45	2026.1
11	Cálculo II	60	2026.2
12	Metodologia Científica	30	2026.1
13	Inteligência Artificial	60	2026.2
14	Compiladores	60	2026.2
15	Computação Gráfica	60	2026.2
\.


--
-- Data for Name: disponibilidade; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.disponibilidade (id_disponibilidade, horario_inicio, horario_final, data_inicio, data_fim, dia_semana, id_monitor) FROM stdin;
1	14:00:00	16:00:00	2026-03-01	2026-06-30	Segunda-feira	1
2	08:00:00	10:00:00	2026-03-01	2026-06-30	Terça-feira	2
3	10:00:00	12:00:00	2026-03-01	2026-06-30	Quarta-feira	3
4	16:00:00	18:00:00	2026-03-01	2026-06-30	Quinta-feira	4
5	14:00:00	16:00:00	2026-03-01	2026-06-30	Sexta-feira	5
6	08:00:00	10:00:00	2026-03-01	2026-06-30	Segunda-feira	6
7	10:00:00	12:00:00	2026-03-01	2026-06-30	Terça-feira	7
8	16:00:00	18:00:00	2026-03-01	2026-06-30	Quarta-feira	8
9	14:00:00	16:00:00	2026-03-01	2026-06-30	Quinta-feira	9
10	08:00:00	10:00:00	2026-03-01	2026-06-30	Sexta-feira	10
11	10:00:00	12:00:00	2026-03-01	2026-06-30	Segunda-feira	11
12	16:00:00	18:00:00	2026-03-01	2026-06-30	Terça-feira	12
13	14:00:00	16:00:00	2026-03-01	2026-06-30	Quarta-feira	13
14	08:00:00	10:00:00	2026-03-01	2026-06-30	Quinta-feira	14
15	10:00:00	12:00:00	2026-03-01	2026-06-30	Sexta-feira	15
\.


--
-- Data for Name: fila_espera; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fila_espera (data_entrada, posicao, id_aluno, id_sessao) FROM stdin;
2026-03-09	1	2	1
2026-03-10	2	3	2
2026-03-11	3	4	3
2026-03-12	4	5	4
2026-03-13	5	6	5
2026-03-14	6	7	6
2026-03-15	7	8	7
2026-03-16	8	9	8
2026-03-17	9	10	9
2026-03-18	10	11	10
2026-03-19	11	12	11
2026-03-20	12	13	12
2026-03-21	13	14	13
2026-03-22	14	15	14
2026-03-23	15	1	15
\.


--
-- Data for Name: frequencia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.frequencia (id_frequencia, presente, hora_entrada, hora_saida, id_aluno, id_sessao) FROM stdin;
1	P	14:05:00	15:55:00	1	1
2	P	08:01:00	09:59:00	2	2
3	F	00:00:00	00:00:00	3	3
4	P	16:02:00	17:50:00	4	4
5	P	14:00:00	16:00:00	5	5
6	P	08:10:00	09:45:00	6	6
7	F	00:00:00	00:00:00	7	7
8	P	16:00:00	18:00:00	8	8
9	P	14:03:00	15:58:00	9	9
10	P	08:00:00	10:00:00	10	10
11	P	10:05:00	11:55:00	11	11
12	F	00:00:00	00:00:00	12	12
13	P	14:00:00	16:00:00	13	13
14	P	08:02:00	09:57:00	14	14
15	P	10:00:00	12:00:00	15	15
\.


--
-- Data for Name: material; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.material (id_material, descricao, titulo, tipo_arquivo, link_arquivo, usuario_id) FROM stdin;
1	Lista de exercícios de limites	Lista 1 Calc	PDF	http://link.com/l1	1
2	Notas de aula de matrizes	Notas Álgebra	PDF	http://link.com/n1	2
3	Slides de introdução a C	Slides Intro C	PPTX	http://link.com/s1	3
4	Código exemplo de Árvores	Exemplo Árvore	ZIP	http://link.com/c1	4
5	Script SQL de criação	Script SQL	SQL	http://link.com/sq1	5
6	Diagrama de Casos de Uso	Diagrama UML	PNG	http://link.com/d1	6
7	Resumo de Gerência de Memória	Resumo SO	PDF	http://link.com/r1	7
8	Apostila de Modelo OSI	Modelo OSI	PDF	http://link.com/a1	8
9	Formulário de Cinemática	Formulário Fís	PDF	http://link.com/f1	9
10	Tabela Periódica PDF	Tabela Per	PDF	http://link.com/t1	10
11	Exercícios Integrais	Lista 2 Calc	PDF	http://link.com/l2	11
12	Manual de Escrita Científica	Manual ABNT	PDF	http://link.com/m1	12
13	Introdução a Redes Neurais	Intro RedesN	PDF	http://link.com/rn	13
14	Gramáticas Livres de Contexto	Slides Compil	PPTX	http://link.com/sc	14
15	Matrizes de Projeção 3D	Notas CompGr	PDF	http://link.com/cg	15
\.


--
-- Data for Name: matricula_se; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.matricula_se (id_aluno, id_disciplina, id_turma) FROM stdin;
1	1	1
2	2	2
3	3	3
4	4	4
5	5	5
6	6	6
7	7	7
8	8	8
9	9	9
10	10	10
11	11	11
12	12	12
13	13	13
14	14	14
15	15	15
\.


--
-- Data for Name: ministra; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ministra (professor_id, disciplina_id) FROM stdin;
1	1
2	2
3	3
4	4
5	5
6	6
7	7
8	8
9	9
10	10
11	11
12	12
13	13
14	14
15	15
\.


--
-- Data for Name: monitor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.monitor (id_monitor, departamento, id_aluno) FROM stdin;
1	Departamento de Computação	1
2	Departamento de Matemática	2
3	Departamento de Computação	3
4	Departamento de Matemática	4
5	Departamento de Computação	5
6	Departamento de Física	6
7	Departamento de Computação	7
8	Departamento de Computação	8
9	Departamento de Matemática	9
10	Departamento de Física	10
11	Departamento de Computação	11
12	Departamento de Computação	12
13	Departamento de Matemática	13
14	Departamento de Computação	14
15	Departamento de Física	15
\.


--
-- Data for Name: monitoria; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.monitoria (id_monitoria, id_monitor, id_disciplina) FROM stdin;
1	1	1
2	2	2
3	3	3
4	4	4
5	5	5
6	6	6
7	7	7
8	8	8
9	9	9
10	10	10
11	11	11
12	12	12
13	13	13
14	14	14
15	15	15
\.


--
-- Data for Name: professor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.professor (id_professor, departamento, usuario_id) FROM stdin;
1	Departamento de Computação	1
2	Departamento de Matemática	2
3	Departamento de Computação	3
4	Departamento de Matemática	4
5	Departamento de Computação	5
6	Departamento de Física	6
7	Departamento de Computação	7
8	Departamento de Computação	8
9	Departamento de Matemática	9
10	Departamento de Física	10
11	Departamento de Computação	11
12	Departamento de Computação	12
13	Departamento de Matemática	13
14	Departamento de Computação	14
15	Departamento de Física	15
\.


--
-- Data for Name: reserva; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reserva (id_reserva, data_reserva, status, id_aluno, id_sessao) FROM stdin;
1	2026-03-09	Confirmada	1	1
2	2026-03-10	Confirmada	2	2
3	2026-03-11	Pendente	3	3
4	2026-03-12	Confirmada	4	4
5	2026-03-13	Cancelada	5	5
6	2026-03-14	Confirmada	6	6
7	2026-03-15	Confirmada	7	7
8	2026-03-16	Pendente	8	8
9	2026-03-17	Confirmada	9	9
10	2026-03-18	Confirmada	10	10
11	2026-03-19	Confirmada	11	11
12	2026-03-20	Cancelada	12	12
13	2026-03-21	Confirmada	13	13
14	2026-03-22	Confirmada	14	14
15	2026-03-23	Confirmada	15	15
\.


--
-- Data for Name: sessao; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sessao (id_sessao, limite_participantes, horario, descricao, data, id_monitoria) FROM stdin;
1	10	14:00:00	Dúvidas sobre limites e derivadas	2026-03-10	1
2	5	08:00:00	Resolução de sistemas lineares	2026-03-11	2
3	15	10:00:00	Prática de laboratório em C	2026-03-12	3
4	8	16:00:00	Exercícios de Alocação Dinâmica	2026-03-13	4
5	12	14:00:00	Modelagem Entidade-Relacionamento	2026-03-14	5
6	10	08:00:00	Revisão de Requisitos de Software	2026-03-15	6
7	7	10:00:00	Discussão sobre Escalonamento	2026-03-16	7
8	10	16:00:00	Cálculos de Máscara de Sub-rede	2026-03-17	8
9	5	14:00:00	Leis de Newton aplicadas	2026-03-18	9
10	15	08:00:00	Estequiometria passo a passo	2026-03-19	10
11	10	10:00:00	Técnicas avançadas de Integração	2026-03-20	11
12	20	16:00:00	Estruturação de Artigos Científicos	2026-03-21	12
13	8	14:00:00	Algoritmos de Busca em Grafos	2026-03-22	13
14	6	08:00:00	Construção de Autômatos Finitos	2026-03-23	14
15	12	10:00:00	Transformações Geométricas 2D	2026-03-24	15
\.


--
-- Data for Name: turma; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.turma (id_turma, semestre, codigo, disciplina_id, horario) FROM stdin;
1	2026.1	TURMA-A	1	08:00:00
2	2026.1	TURMA-B	2	10:00:00
3	2026.1	TURMA-C	3	14:00:00
4	2026.1	TURMA-D	4	16:00:00
5	2026.2	TURMA-E	5	08:00:00
6	2026.2	TURMA-F	6	10:00:00
7	2026.2	TURMA-G	7	14:00:00
8	2026.2	TURMA-H	8	16:00:00
9	2026.1	TURMA-I	9	08:00:00
10	2026.1	TURMA-J	10	10:00:00
11	2026.2	TURMA-K	11	14:00:00
12	2026.1	TURMA-L	12	16:00:00
13	2026.2	TURMA-M	13	08:00:00
14	2026.2	TURMA-N	14	10:00:00
15	2026.2	TURMA-O	15	14:00:00
\.


--
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuario (id_user, nome, email) FROM stdin;
1	Ana Silva	ana.silva@email.com
2	Bruno Souza	bruno.souza@email.com
3	Carlos Lima	carlos.lima@email.com
4	Diana Prado	diana.prado@email.com
5	Eduardo Costa	eduardo.costa@email.com
6	Fernanda Dias	fernanda.dias@email.com
7	Gabriel Alves	gabriel.alves@email.com
8	Helena Ribeiro	helena.ribeiro@email.com
9	Igor Martins	igor.martins@email.com
10	Julia Carvalho	julia.carvalho@email.com
11	Lucas Melo	lucas.melo@email.com
12	Mariana Santos	mariana.santos@email.com
13	Neto Oliveira	neto.oliveira@email.com
14	Olivia Castro	olivia.castro@email.com
15	Pedro Rocha	pedro.rocha@email.com
\.


--
-- Data for Name: validacao; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.validacao (id_validacao, data_validacao, total_horas, status_validacao, id_professor, id_monitor) FROM stdin;
1	2026-06-15	60	Aprovado	1	1
2	2026-06-15	55	Aprovado	2	2
3	2026-06-15	60	Aprovado	3	3
4	2026-06-15	40	Pendente	4	4
5	2026-06-15	60	Aprovado	5	5
6	2026-06-15	50	Aprovado	6	6
7	2026-06-15	60	Aprovado	7	7
8	2026-06-15	30	Rejeitado	8	8
9	2026-06-15	60	Aprovado	9	9
10	2026-06-15	60	Aprovado	10	10
11	2026-06-15	45	Aprovado	11	11
12	2026-06-15	60	Pendente	12	12
13	2026-06-15	60	Aprovado	13	13
14	2026-06-15	58	Aprovado	14	14
15	2026-06-15	60	Aprovado	15	15
\.


--
-- Name: aluno_id_aluno_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.aluno_id_aluno_seq', 15, true);


--
-- Name: avisos_id_aviso_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.avisos_id_aviso_seq', 15, true);


--
-- Name: certificado_id_certificado_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.certificado_id_certificado_seq', 15, true);


--
-- Name: disciplina_id_disciplina_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.disciplina_id_disciplina_seq', 15, true);


--
-- Name: disponibilidade_id_disponibilidade_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.disponibilidade_id_disponibilidade_seq', 15, true);


--
-- Name: fila_espera_posicao_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fila_espera_posicao_seq', 15, true);


--
-- Name: frequencia_id_frequencia_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.frequencia_id_frequencia_seq', 15, true);


--
-- Name: material_id_material_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.material_id_material_seq', 15, true);


--
-- Name: monitor_id_monitor_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.monitor_id_monitor_seq', 15, true);


--
-- Name: monitoria_id_monitoria_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.monitoria_id_monitoria_seq', 15, true);


--
-- Name: professor_id_professor_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.professor_id_professor_seq', 15, true);


--
-- Name: reserva_id_reserva_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reserva_id_reserva_seq', 15, true);


--
-- Name: sessao_id_sessao_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sessao_id_sessao_seq', 15, true);


--
-- Name: turma_id_turma_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.turma_id_turma_seq', 15, true);


--
-- Name: usuario_id_user_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuario_id_user_seq', 15, true);


--
-- Name: validacao_id_validacao_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.validacao_id_validacao_seq', 15, true);


--
-- Name: aluno aluno_cpf_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aluno
    ADD CONSTRAINT aluno_cpf_key UNIQUE (cpf);


--
-- Name: aluno aluno_matricula_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aluno
    ADD CONSTRAINT aluno_matricula_key UNIQUE (matricula);


--
-- Name: aluno aluno_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aluno
    ADD CONSTRAINT aluno_pkey PRIMARY KEY (id_aluno);


--
-- Name: avisos avisos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avisos
    ADD CONSTRAINT avisos_pkey PRIMARY KEY (id_aviso);


--
-- Name: certificado certificado_codigo_autentificacao_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.certificado
    ADD CONSTRAINT certificado_codigo_autentificacao_key UNIQUE (codigo_autentificacao);


--
-- Name: certificado certificado_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.certificado
    ADD CONSTRAINT certificado_pkey PRIMARY KEY (id_certificado);


--
-- Name: disciplina disciplina_nome_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.disciplina
    ADD CONSTRAINT disciplina_nome_key UNIQUE (nome);


--
-- Name: disciplina disciplina_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.disciplina
    ADD CONSTRAINT disciplina_pkey PRIMARY KEY (id_disciplina);


--
-- Name: disponibilidade disponibilidade_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.disponibilidade
    ADD CONSTRAINT disponibilidade_pkey PRIMARY KEY (id_disponibilidade);


--
-- Name: fila_espera fila_espera_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fila_espera
    ADD CONSTRAINT fila_espera_pkey PRIMARY KEY (id_aluno, id_sessao);


--
-- Name: frequencia frequencia_aluno_sessao_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.frequencia
    ADD CONSTRAINT frequencia_aluno_sessao_key UNIQUE (id_aluno, id_sessao);


--
-- Name: frequencia frequencia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.frequencia
    ADD CONSTRAINT frequencia_pkey PRIMARY KEY (id_frequencia);


--
-- Name: material material_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.material
    ADD CONSTRAINT material_pkey PRIMARY KEY (id_material);


--
-- Name: matricula_se matricula_se_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matricula_se
    ADD CONSTRAINT matricula_se_pkey PRIMARY KEY (id_aluno, id_disciplina, id_turma);


--
-- Name: ministra ministra_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ministra
    ADD CONSTRAINT ministra_pkey PRIMARY KEY (professor_id, disciplina_id);


--
-- Name: monitor monitor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monitor
    ADD CONSTRAINT monitor_pkey PRIMARY KEY (id_monitor);


--
-- Name: monitoria monitoria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monitoria
    ADD CONSTRAINT monitoria_pkey PRIMARY KEY (id_monitoria);


--
-- Name: professor professor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professor
    ADD CONSTRAINT professor_pkey PRIMARY KEY (id_professor);


--
-- Name: reserva reserva_aluno_sessao_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reserva
    ADD CONSTRAINT reserva_aluno_sessao_key UNIQUE (id_aluno, id_sessao);


--
-- Name: reserva reserva_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reserva
    ADD CONSTRAINT reserva_pkey PRIMARY KEY (id_reserva);


--
-- Name: sessao sessao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessao
    ADD CONSTRAINT sessao_pkey PRIMARY KEY (id_sessao);


--
-- Name: turma turma_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.turma
    ADD CONSTRAINT turma_pkey PRIMARY KEY (id_turma);


--
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id_user);


--
-- Name: validacao validacao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.validacao
    ADD CONSTRAINT validacao_pkey PRIMARY KEY (id_validacao);


--
-- Name: fila_espera fk_aluno; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fila_espera
    ADD CONSTRAINT fk_aluno FOREIGN KEY (id_aluno) REFERENCES public.aluno(id_aluno);


--
-- Name: frequencia fk_aluno; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.frequencia
    ADD CONSTRAINT fk_aluno FOREIGN KEY (id_aluno) REFERENCES public.aluno(id_aluno);


--
-- Name: matricula_se fk_aluno; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matricula_se
    ADD CONSTRAINT fk_aluno FOREIGN KEY (id_aluno) REFERENCES public.aluno(id_aluno);


--
-- Name: monitor fk_aluno; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monitor
    ADD CONSTRAINT fk_aluno FOREIGN KEY (id_aluno) REFERENCES public.aluno(id_aluno);


--
-- Name: reserva fk_aluno; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reserva
    ADD CONSTRAINT fk_aluno FOREIGN KEY (id_aluno) REFERENCES public.aluno(id_aluno);


--
-- Name: matricula_se fk_disciplina; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matricula_se
    ADD CONSTRAINT fk_disciplina FOREIGN KEY (id_disciplina) REFERENCES public.disciplina(id_disciplina);


--
-- Name: ministra fk_disciplina; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ministra
    ADD CONSTRAINT fk_disciplina FOREIGN KEY (disciplina_id) REFERENCES public.disciplina(id_disciplina);


--
-- Name: monitoria fk_disciplina; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monitoria
    ADD CONSTRAINT fk_disciplina FOREIGN KEY (id_disciplina) REFERENCES public.disciplina(id_disciplina);


--
-- Name: turma fk_disciplina; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.turma
    ADD CONSTRAINT fk_disciplina FOREIGN KEY (disciplina_id) REFERENCES public.disciplina(id_disciplina);


--
-- Name: certificado fk_monitor; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.certificado
    ADD CONSTRAINT fk_monitor FOREIGN KEY (id_monitor) REFERENCES public.monitor(id_monitor);


--
-- Name: disponibilidade fk_monitor; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.disponibilidade
    ADD CONSTRAINT fk_monitor FOREIGN KEY (id_monitor) REFERENCES public.monitor(id_monitor);


--
-- Name: monitoria fk_monitor; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monitoria
    ADD CONSTRAINT fk_monitor FOREIGN KEY (id_monitor) REFERENCES public.monitor(id_monitor);


--
-- Name: validacao fk_monitor; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.validacao
    ADD CONSTRAINT fk_monitor FOREIGN KEY (id_monitor) REFERENCES public.monitor(id_monitor);


--
-- Name: sessao fk_monitoria; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessao
    ADD CONSTRAINT fk_monitoria FOREIGN KEY (id_monitoria) REFERENCES public.monitoria(id_monitoria);


--
-- Name: ministra fk_professor; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ministra
    ADD CONSTRAINT fk_professor FOREIGN KEY (professor_id) REFERENCES public.professor(id_professor);


--
-- Name: validacao fk_professor; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.validacao
    ADD CONSTRAINT fk_professor FOREIGN KEY (id_professor) REFERENCES public.professor(id_professor);


--
-- Name: fila_espera fk_sessao; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fila_espera
    ADD CONSTRAINT fk_sessao FOREIGN KEY (id_sessao) REFERENCES public.sessao(id_sessao);


--
-- Name: frequencia fk_sessao; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.frequencia
    ADD CONSTRAINT fk_sessao FOREIGN KEY (id_sessao) REFERENCES public.sessao(id_sessao);


--
-- Name: reserva fk_sessao; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reserva
    ADD CONSTRAINT fk_sessao FOREIGN KEY (id_sessao) REFERENCES public.sessao(id_sessao);


--
-- Name: matricula_se fk_turma; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matricula_se
    ADD CONSTRAINT fk_turma FOREIGN KEY (id_turma) REFERENCES public.turma(id_turma);


--
-- Name: aluno fk_usuario; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aluno
    ADD CONSTRAINT fk_usuario FOREIGN KEY (id_usuario) REFERENCES public.usuario(id_user);


--
-- Name: avisos fk_usuario; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avisos
    ADD CONSTRAINT fk_usuario FOREIGN KEY (usuario_id) REFERENCES public.usuario(id_user);


--
-- Name: material fk_usuario; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.material
    ADD CONSTRAINT fk_usuario FOREIGN KEY (usuario_id) REFERENCES public.usuario(id_user);


--
-- Name: professor fk_usuario; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professor
    ADD CONSTRAINT fk_usuario FOREIGN KEY (usuario_id) REFERENCES public.usuario(id_user);


--
-- PostgreSQL database dump complete
--

\unrestrict YuZpm4NdAcTY3DhJwEQ40yo27gx1mkQACyQy8iXk7mHIIlsxyRkVepUX6BlstV7

