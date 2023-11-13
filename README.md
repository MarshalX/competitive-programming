# Competitive Programming ![WakaTime](https://wakatime.com/badge/user/3dffa020-4a1a-4dcc-8526-a337c2321c39/project/68016cf3-c5b4-4085-b9fa-85bf43920f0f.svg?style=flat-square)

> Я просто хочу пройти алгоритмический собес 🥺

Тут будут какие-то заметки, когда я столкнусь с чем-то сложным/интересным/новым для себя.

Кроме этого сформирую базу ссылок того что читал/смотрел/изучал.

На текущий момент основная платформа LeetCode.

## Алгоритмы

- **KMP** — поиск подстроки в строке за O(m + n). Встретился в [28](https://github.com/MarshalX/competitive-programming/blob/6b2a5be0d03e7b7219645f8841f24beba80f036c/main.cpp). [Брутфорс](https://github.com/MarshalX/competitive-programming/blob/614c1ef638e04804b348ad9463c20f4e8378e32f/main.cpp) ушёл в TL. Алгос списал с псевдокода на вики: [Knuth–Morris–Pratt algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm).
- **Prefix sum** — [быстрый ответ](https://github.com/MarshalX/competitive-programming/blob/b86ddc27fc22820f2fc1d3e4008ddc2c2471e454/main.cpp) на множество вопросов "Какая сумма на подмассиве от L до R?" (pref[0] = a[0]; pref[i] = pref[i - 1] + a[i]. Q: pref[r] - pref[l - 1] или pref[r] если l == 0). Точ в точ задача [303](https://github.com/MarshalX/competitive-programming/blob/b815c2340153d415895e18e8899f0a226c08de54/main.cpp). Интересное и легкое усложнение задачи в [724](https://github.com/MarshalX/competitive-programming/blob/a507ae4e8671bd6b49eaaa2c9a5e9c8d69b1f5d3/main.cpp).
- **Kadane's algorithm** — подмассив с [наибольшей суммой](https://github.com/MarshalX/competitive-programming/blob/7ab975a6852e5a156f724c54e15bbf8316dcc0d7/main.cpp) (tSum += a[i]; tSum = max(tSum, a[i]); res = max(res, tSum)).

## Заметки

- В [1408](https://github.com/MarshalX/competitive-programming/blob/58a7bf680ee220d3f61ae5646616178f0f790ddc/main.cpp) допустил ошибку при оценке временной сложности. Там не O(N^2\*L), а O(N\*L), где L сумма длин всех строк. Потому что несмотря на вложенный цикл мы выполняем поиск в строке за длину строку, а циклы порождают сравнение строки с каждой другой. Где каждую другую можно заменить на сумму длин всех строк (L). Поэтому оценка количество строк умноженное на сумму длин (N*L). Что меньше моей изначальной оценки, так как в условии задачи максимальная длинна строк 30, а количество слов 100.
- Долго мучался с [11](https://github.com/MarshalX/competitive-programming/blob/f96b815b378244118cc62b853dd1bc79579aad16/main.cpp) (бассейн с двумя бортиками). [Брутфорс](https://github.com/MarshalX/competitive-programming/blob/eea774a355ef010ab415128eb5095d2616fdc5d6/main.cpp) конечно не зашёл, прочитал подсказки, частично дорешал, не справившись отловить баг пошёл в обсуждения к задаче. Посмотря на чужой код понял, что нафантазировал ненужные дополнительные условия ([diff](https://github.com/MarshalX/competitive-programming/commit/f96b815b378244118cc62b853dd1bc79579aad16#diff-608d8de3fba954c50110b6d7386988f27295de845e9d7174e40095ba5efcf1bb)). В итоге списал с чужого кода, но свою ошибку понял (кажется). Upd. [121](https://github.com/MarshalX/competitive-programming/blob/3996845fd582109d7b4cfe1a8d2db40e7bc8a615/main.cpp) задача мне сильно напомнила эту.
- В [1337](https://github.com/MarshalX/competitive-programming/blob/1f8a3934f4e0e50da6c3330208279d819da8652c/main.cpp) первый раз использовал кучу. В условии задачи условия повторяют сравнение пары интов. Если первые элементы (сила строки AKA кол-во единиц в ней) равны, то сравниваем вторые (индекс в массиве по задаче). Так как по условию нам нужно вывести слабейших, то используем кучу для поиска **минимума** (`std::priority_queue<T, vector<T>, greater<T>>`).
- В [231](https://github.com/MarshalX/competitive-programming/blob/fc874758789e1703255246c1dc9cbd63187a43a2/main.cpp) сраные граничные случаи с -2^31 и 2^31-1.

## Ссылки на почитать
- [x] [Maximum subarray problem (Kadane's algorithm)](https://en.wikipedia.org/wiki/Maximum_subarray_problem). LeetCode [53](https://leetcode.com/problems/maximum-subarray/)
- [ ] [Sliding Window Technique](https://quanticdev.com/algorithms/dynamic-programming/sliding-window/)
- [x] [Префиксные суммы. XOR. Задачи на запросы](https://brestprog.by/topics/prefixsums/)
- [x] [Полное бинарное дерево. Куча. Очередь с приоритетом](https://brestprog.by/topics/heap/)
- [ ] [Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight). LeetCode [191](https://github.com/MarshalX/competitive-programming/blob/b05daa0e7889065671c62d4a3267d08e5f94eea7/main.cpp) 
- [ ] [Custom impl of `__builtin_popcount`](https://stackoverflow.com/questions/52161596/why-is-builtin-popcount-slower-than-my-own-bit-counting-function/52161813) 
- [ ] [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance)
- [ ] [How to count leading zeros in integer (`__builtin_clz` and pure impls)](https://stackoverflow.com/questions/23856596/how-to-count-leading-zeros-in-a-32-bit-unsigned-integer)

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
- [What is Bitmasking](https://youtu.be/7FmL-WpTTJ4)
- [Bitwise Operations tutorial #1 | XOR, Shift, Subsets](https://youtu.be/xXKL9YBWgCY)
- Плейлист [АиСД year2020 s1](https://youtube.com/playlist?list=PLrS21S1jm43jz48qjdfYNpuIPgL3lNJ_o)
- Что такое sliding window: [Solve subarray problems FASTER (using Sliding Windows)](https://youtu.be/GcW4mgmgSbw)
- Что такое dynamic programming: [Mastering Dynamic Programming - How to solve any interview problem (Part 1)](https://youtu.be/Hdr64lKQ3e4)
- [Linked List Cycle - Floyd's Tortoise and Hare](https://youtu.be/gBTe7lFR3vc)
- Найти позицию начала цикла (`len(head -> cycle_start) == len(equal_pointers -> cycle_start)`) [Floyd's Cycle Detection](https://youtu.be/wjYnzkAhcNk)
- [How Dijkstra's Algorithm Works](https://youtu.be/EFg3u_E6eHU)
