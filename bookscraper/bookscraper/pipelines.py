# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        # Strip all whitespaces from strings
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name != "description":
                value = adapter.get(field_name)
                adapter[field_name] = value[0].strip()

        # lowercase value in "category" and "product_type"
        lowercase_keys = ["category", "product_type"]
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower()

        # convert price to float and removed currency sign
        price_keys = ["price", "price_excl_tax", "price_incl_tax", "tax"]
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace("£", "")
            adapter[price_key] = float(value)

        # convert availability to number
        availability_string = adapter.get("availability")
        split_string_array = availability_string.split("(")
        if len(split_string_array) < 2:
            adapter["availability"] = 0
        else:
            availability_array = split_string_array[1].split(" ")
            adapter["availability"] = int(availability_array[0])

        # convert reviews to number
        num_reviews_string = adapter.get("num_reviews")
        adapter["num_reviews"] = int(num_reviews_string)

        # convert stars rating to number
        stars_rating = adapter.get("stars").lower()
        if stars_rating == "zero":
            adapter["stars"] = 0
        elif stars_rating == "one":
            adapter["stars"] = 1
        elif stars_rating == "two":
            adapter["stars"] = 2
        elif stars_rating == "three":
            adapter["stars"] = 3
        elif stars_rating == "four":
            adapter["stars"] = 4
        else:
            adapter["stars"] = 5

        return item
