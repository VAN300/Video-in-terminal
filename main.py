#!/usr/bin/env python
# encoding: utf-8

from handler import video


def main():
    path: str = input()
    video.collect_video(path)


if __name__ == '__main__':
    main()
