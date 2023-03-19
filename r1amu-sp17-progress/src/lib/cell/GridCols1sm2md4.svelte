<script>
    let className;
    export { className as class };
</script>

<div class="a {className}">
    <slot />
</div>

<style lang="postcss" module>
    .a {
        @apply grid grid-cols-1;
    }
    @media (min-width: 640px) {
        .a {
            @apply grid-cols-2;
        }
    }
    @media (min-width: 768px) {
        .a {
            @apply grid-cols-4;
        }
    }
</style>
