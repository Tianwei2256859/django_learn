#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
PAGINATOR_NUM_PER_PAGE = 10


def pagination(objects, page, page_size=PAGINATOR_NUM_PER_PAGE):
    paginator = LocalPaginator(objects, page_size)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    return objects


class LocalPaginator(Paginator):
    def page(self, number):
        """
        Returns a Page object for the given 1-based page number.
        """
        number = self.validate_number(number)
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        if top + self.orphans >= self.count:
            top = self.count
        self.number = number
        return self._get_page(self.object_list[bottom:top], number, self)

    def page_list_show(self):
        return self.get_pages_range(self.num_pages, self.number)

    @staticmethod
    def get_pages_range(m, cur_page):
        PER_PRE_NUM = 6
        PER_NUMBER_MAX = 10
        if m > PER_NUMBER_MAX:
            limit_start = 1 if cur_page <= PER_PRE_NUM else cur_page - (PER_PRE_NUM - 1)

            if m >= cur_page + (PER_PRE_NUM - 2):
                if cur_page >= PER_PRE_NUM:
                    limit_end = m - limit_start if cur_page < PER_PRE_NUM else cur_page + (PER_PRE_NUM - 2)
                else:
                    limit_end = PER_NUMBER_MAX
            else:
                limit_end = m
                if cur_page >= PER_NUMBER_MAX or ((limit_end - limit_start) < PER_NUMBER_MAX):
                    limit_start = limit_end - (PER_NUMBER_MAX - 1)

        else:
            limit_start, limit_end = 1, m
        return xrange(limit_start, limit_end + 1)
