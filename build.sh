#!/usr/bin/env bash

# 1. প্রয়োজনীয় প্যাকেজ ইনস্টল
pip install -r requirements.txt

# 2. Static ফাইল কালেক্ট
python manage.py collectstatic --noinput

# 3. ডাটাবেজ মাইগ্রেশন চালানো
python manage.py migrate
