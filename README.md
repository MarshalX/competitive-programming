# LeetCode

> Я просто хочу пройти алгоритмический собес 🥺

Тут будут какие-то заметки, когда я столкнусь с чем-то сложным/интересным/новым для себя.

Кроме этого сформирую базу ссылок того что читал/смотрел/изучал.

## Алгоритмы

- **KMP** — поиск подстроки в строке за O(m + n). Встретился в [28](https://github.com/MarshalX/LeetCode/blob/6b2a5be0d03e7b7219645f8841f24beba80f036c/main.cpp). [Брутфорс](https://github.com/MarshalX/LeetCode/blob/614c1ef638e04804b348ad9463c20f4e8378e32f/main.cpp) ушёл в TL. Алгос списал с псевдокода на вики: [Knuth–Morris–Pratt algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm).
- **Prefix sum** — [быстрый ответ](https://github.com/MarshalX/LeetCode/blob/b86ddc27fc22820f2fc1d3e4008ddc2c2471e454/main.cpp) на множество вопросов "Какая сумма на подмассиве от L до R?" (pref[0] = a[0]; pref[i] = pref[i - 1] + a[i]. Q: pref[r] - pref[l -1] или pref[r] если l == 0).
- **Kadane's algorithm** — TODO.

## Заметки

- В [1408](https://github.com/MarshalX/LeetCode/blob/58a7bf680ee220d3f61ae5646616178f0f790ddc/main.cpp) допустил ошибку при оценке временной сложности. Там не O(N^2\*L), а O(N\*L), где L сумма длин всех строк. Потому что несмотря на вложенный цикл мы выполняем поиск в строке за длину строку, а циклы порождают сравнение строки с каждой другой. Где каждую другую можно заменить на сумму длин всех строк (L). Поэтому оценка количество строк умноженное на сумму длин (N*L). Что меньше моей изначальной оценки, так как в условии задачи максимальная длинна строк 30, а количество слов 100.
- Долго мучался с [11](https://github.com/MarshalX/LeetCode/blob/f96b815b378244118cc62b853dd1bc79579aad16/main.cpp) (бассейн с двумя бортиками). [Брутфорс](https://github.com/MarshalX/LeetCode/blob/eea774a355ef010ab415128eb5095d2616fdc5d6/main.cpp) конечно не зашёл, прочитал подсказки, частично дорешал, не справившись отловить баг пошёл в обсуждения к задаче. Посмотря на чужой код понял, что нафантазировал ненужные дополнительные условия ([diff](https://github.com/MarshalX/LeetCode/commit/f96b815b378244118cc62b853dd1bc79579aad16#diff-608d8de3fba954c50110b6d7386988f27295de845e9d7174e40095ba5efcf1bb)). В итоге списал с чужого кода, но свою ошибку понял (кажется).

## Ссылки на почитать
- [ ] [Maximum subarray problem (Kadane's algorithm)](https://en.wikipedia.org/wiki/Maximum_subarray_problem). LeetCode [53](https://leetcode.com/problems/maximum-subarray/)
- [ ] [Sliding Window Technique](https://quanticdev.com/algorithms/dynamic-programming/sliding-window/)
- [x] [Префиксные суммы. XOR. Задачи на запросы](https://brestprog.by/topics/prefixsums/)

## Ссылки на посмотреть
- [Четыре задачи на два указателя](https://youtu.be/MyWNZJ10zIU)
- [Алгоритм Кнута-Морриса-Пратта](https://youtu.be/7g-WEBj3igk)
- [Динамическое программирование это просто](https://youtu.be/GOF4VUi4nGU)
- [Задача о рюкзаке. Динамическое программирование](https://youtu.be/AgM-w6QuIHQ)
- [Прямая и обратная польская нотация](https://youtu.be/sC566vzV9B0)
- [Популярная в собеседованиях гугл задача. Разбор и решение (Guess the word 843 на LeetCode)](https://youtu.be/pJNd7AzIWGc)
- [Хитрая задача на Стек](https://youtu.be/-59FbGWsCgI)
- [Поиск Знаменитости. Метод двух указателей](https://youtu.be/xGvQN_g-JCI)
- [Динамическое Программирование: Количество Уникальных Путей](https://youtu.be/GhiRlhPlJ9Q)
