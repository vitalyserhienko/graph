### Example of django versatileimagefield with graphql
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `add some products with images`
- `python manage.py runserver` 
- `http://localhost:8000/graphql/`

### Request example
```query {
  products {
    images {
      id
      image
      sizedImage (size: "200x200")
    }
  }
}
```
### Response example
```json
{
  "data": {
    "products": [
      {
        "images": [
          {
            "id": "2",
            "image": "product/images/nexus_5.jpg",
            "sizedImage": "/media/__sized__/product/images/nexus_5-thumbnail-200x200-70.jpg"
          }
        ]
      },
      {
        "images": [
          {
            "id": "3",
            "image": "product/images/galaxy_s7.jpg",
            "sizedImage": "/media/__sized__/product/images/galaxy_s7-thumbnail-200x200-70.jpg"
          }
        ]
      }
    ]
  }
}
```
