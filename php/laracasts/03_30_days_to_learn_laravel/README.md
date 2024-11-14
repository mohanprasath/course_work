# 30 Days to Learn Laravel

## 01 Hello, Laravel, 02 Your First Route and View, 03 Create a Layout File Using Laravel Components

- Use `Laravel herd` application for one click php and other laravel apps
- run `laravel new 01_example` to create a new laravel project
- run `php artisan serve` to start the server
- `*.blade.php` files are used to create views in laravel and are stored in `resources/views` directory
- `Components` folder is used to store reusable components in laravel i.e. layouts, headers, footers etc.
- `<x-layout>` is used to include a layout component in a view using the `{{ $slot }}` directive
- prop or named slot can be passed to a component using the `{{ $slot }}` directive
- `x-layout` component can be used to create a layout file in laravel
- `x-header` and `x-footer` components can be used to create header and footer components in laravel