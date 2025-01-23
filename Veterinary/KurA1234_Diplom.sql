-- phpMyAdmin SQL Dump
-- version 4.9.4
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Янв 23 2025 г., 14:19
-- Версия сервера: 8.0.13
-- Версия PHP: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `KurA1234_Diplom`
--

-- --------------------------------------------------------

--
-- Структура таблицы `list_of_services`
--

CREATE TABLE `list_of_services` (
  `id` int(11) NOT NULL,
  `services` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `price` varchar(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `list_of_services`
--

INSERT INTO `list_of_services` (`id`, `services`, `price`) VALUES
(1, 'Гигиеническая стрижка животных, уход за шерстью, когтями и зубами', '2000руб.'),
(2, 'Консультации по вопросам рациона питомца, советы по правильному подбору сухого или натурального корма', 'бесплатно'),
(3, 'Проведение анализов для определения текущего состояния здоровья животного.', '1500руб.'),
(4, 'Вакцинация новорожденных детенышей или взрослых особей', '5000руб.'),
(5, 'Чипирование животного', '2000руб.');

-- --------------------------------------------------------

--
-- Структура таблицы `reception_shedule`
--

CREATE TABLE `reception_shedule` (
  `id` int(11) NOT NULL,
  `date_of_admission` datetime NOT NULL,
  `client` varchar(11) NOT NULL,
  `staff_id` int(10) UNSIGNED NOT NULL,
  `services_id` int(10) UNSIGNED NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `reception_shedule`
--

INSERT INTO `reception_shedule` (`id`, `date_of_admission`, `client`, `staff_id`, `services_id`) VALUES
(8, '2024-12-12 17:00:00', 'Дима', 1, 1),
(7, '2024-12-12 17:00:00', 'Олег', 1, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `role`
--

CREATE TABLE `role` (
  `id` int(11) UNSIGNED NOT NULL,
  `role` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `role`
--

INSERT INTO `role` (`id`, `role`) VALUES
(1, 'veterinarian'),
(2, 'admin');

-- --------------------------------------------------------

--
-- Структура таблицы `staff`
--

CREATE TABLE `staff` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `role_id` int(11) NOT NULL,
  `login` varchar(11) NOT NULL,
  `password` varchar(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `staff`
--

INSERT INTO `staff` (`id`, `name`, `role_id`, `login`, `password`) VALUES
(1, 'Дмитрий', 2, 'Admin', 'Admin'),
(2, 'Виктория', 1, 'Vet1', 'Vet1'),
(3, 'Мария', 1, 'Vet2', 'Vet2');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `list_of_services`
--
ALTER TABLE `list_of_services`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `reception_shedule`
--
ALTER TABLE `reception_shedule`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `list_of_services`
--
ALTER TABLE `list_of_services`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `reception_shedule`
--
ALTER TABLE `reception_shedule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT для таблицы `role`
--
ALTER TABLE `role`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `staff`
--
ALTER TABLE `staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
