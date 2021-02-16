from django import template

register = template.Library()

@register.filter
def sub(value, arg):
  # 기존값 value 에 입력으로 받은 값 arg
  return value - arg