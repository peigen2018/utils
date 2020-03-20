package com.niceol.picklessons.common.utils;

import java.text.MessageFormat;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

import org.apache.commons.lang.StringUtils;
import org.apache.commons.lang.time.DateFormatUtils;
import org.apache.commons.lang.time.DateUtils;

import com.niceol.picklessons.common.exception.RRException;

public class DateTimeUtils {

    public static Date parseDate(String date, String... parsePatterns) {
        try {
            return DateUtils.parseDate(date, parsePatterns);
        } catch (ParseException e) {
            throw new RRException("convert error", e);
        }
    }

    /**
     * 时间format类
     * @param startDate 开始时间
     * @param hours 课时
     * @param weekOfDays 星期 [0,1,2] 代表周日 周一 周二
     * @param startTime 无任何作用 只为拼接
     * @param endTime 无任何作用 只为拼接
     * @return 返回format后字符串 {0}~{1} 每周{2} {3}~{4}     
     */
    public static String courseTimeformat(Date startDate, Integer hours, Integer[] weekOfDays, String startTime,
            String endTime) {

        Calendar endDateCal = Calendar.getInstance();
        endDateCal.setTime(startDate);
        endDateCal.get(Calendar.WEEK_OF_YEAR);
        Integer week = hours / weekOfDays.length;
        endDateCal.add(Calendar.WEEK_OF_YEAR, week);
        int mod = hours % weekOfDays.length;

        if (mod != 0) {
            int lastDayOfWeek = weekOfDays[mod - 1];
            int weekT = coverWeek(endDateCal.get(Calendar.DAY_OF_WEEK));
            while (weekT != lastDayOfWeek) {
                endDateCal.add(Calendar.DATE, 1);
                weekT = coverWeek(endDateCal.get(Calendar.DAY_OF_WEEK));
                System.out.println(weekT);
            }
        }

        List<String> weekTexts = new ArrayList<>();
        for (int weekOfDay : weekOfDays) {
            weekTexts.add(coverWeekToText(weekOfDay));
        }

        return MessageFormat.format("{0}~{1} 每周{2} {3}~{4}", DateFormatUtils.format(startDate, "MM月dd日"),
                DateFormatUtils.format(endDateCal, "MM月dd日 "), StringUtils.join(weekTexts, ","), startTime, endTime);
    }

    /**
     * 系统日期week代表数字转换成参数week代表数字
     * 
     * @param week 周
     * @return 转换后周
     */
    public static int coverWeek(int week) {
        switch (week) {
        case Calendar.SUNDAY:
            return 0;
        case Calendar.MONDAY:
            return 1;
        case Calendar.TUESDAY:
            return 2;
        case Calendar.WEDNESDAY:
            return 3;
        case Calendar.THURSDAY:
            return 4;
        case Calendar.FRIDAY:
            return 5;
        case Calendar.SATURDAY:
            return 6;
        default:
            throw new RRException("un support");
        }
    }

    public static String coverWeekToText(int week) {
        switch (week) {
        case 0:
            return "日";
        case 1:
            return "一";
        case 2:
            return "二";
        case 3:
            return "三";
        case 4:
            return "四";
        case 5:
            return "五";
        case 6:
            return "六";
        default:
            throw new RRException("un support");
        }
    }
}
