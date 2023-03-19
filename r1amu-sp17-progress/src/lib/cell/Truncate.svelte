<script>
    let className;
    export { className as class };
</script>

<p class="a {className}">
    <slot />
</p>

<style lang="postcss" module>
    .a {
        @apply truncate;
    }
</style>
